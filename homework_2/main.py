import argparse
import subprocess
import yaml
from datetime import datetime, timezone, timedelta
from typing import Dict, List


class GitObject:
    def __init__(self, sha1: str, obj_type: str, content: bytes):
        self.sha1 = sha1
        self.type = obj_type
        self.content = content.decode('utf-8', errors='replace')


class CommitNode:
    def __init__(self, sha1: str, author: str, date: str, message: str, parents: List[str]):
        self.sha1 = sha1
        self.author = author
        self.date = date
        self.message = message
        self.parents = parents


def parse_config(config_path: str) -> Dict[str, str]:
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return {
        'repo_path': config['repo_path'],
        'output_path': config['output_path'],
        'start_date': config['start_date'],
    }


def get_commits_since_date(repo_path: str, start_date: str) -> List[str]:
    result = subprocess.run(
        ['git', 'rev-list', '--since', start_date, '--all'],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError("Error retrieving commits.")

    return result.stdout.splitlines()


def read_object(repo_path: str, sha1: str) -> GitObject:
    result = subprocess.run(
        ['git', 'cat-file', '-p', sha1],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise FileNotFoundError(f"Object '{sha1}' not found.")

    type_result = subprocess.run(
        ['git', 'cat-file', '-t', sha1],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    obj_type = type_result.stdout.strip()

    return GitObject(sha1, obj_type, result.stdout.encode('utf-8'))


def parse_commit(obj: GitObject) -> CommitNode:
    lines = obj.content.split('\n')
    parents = []
    author = ''
    date = ''
    message = ''
    in_message = False
    for line in lines:
        if line.startswith('parent '):
            parents.append(line[7:])
        elif line.startswith('author '):
            author_info = line[7:]
            author_parts = author_info.rsplit(' ', 2)
            author_name_email = author_parts[0]
            timestamp = int(author_parts[1])
            timezone_str = author_parts[2]
            tz_sign = 1 if timezone_str.startswith('+') else -1
            tz_hours = int(timezone_str[1:3])
            tz_minutes = int(timezone_str[3:5])
            tz_offset = tz_sign * timedelta(hours=tz_hours, minutes=tz_minutes)
            dt = datetime.fromtimestamp(timestamp, tz=timezone(tz_offset))
            date_time = dt.strftime('%Y-%m-%d %H:%M:%S %z')
            author = author_name_email
            date = date_time
        elif line == '':
            in_message = True
        elif in_message:
            message += line + '\n'
    return CommitNode(obj.sha1, author, date, message.strip(), parents)


def is_date_after(date1: str, date2: str) -> bool:
    y1, m1, d1 = map(int, date1.split('-'))
    y2, m2, d2 = map(int, date2.split('-'))

    if y1 != y2:
        return y1 > y2
    if m1 != m2:
        return m1 > m2
    return d1 > d2


def build_commit_graph(repo_path: str, start_date: str) -> Dict[str, CommitNode]:
    commit_sha1s = get_commits_since_date(repo_path, start_date)
    graph = {}

    for sha1 in commit_sha1s:
        obj = read_object(repo_path, sha1)
        if obj.type != 'commit':
            continue

        commit_node = parse_commit(obj)

        commit_date_str = commit_node.date.split(' ')[0]
        if is_date_after(commit_date_str, start_date):
            graph[sha1] = commit_node

            for parent_sha1 in commit_node.parents:
                parent_obj = read_object(repo_path, parent_sha1)
                if parent_obj.type != 'commit':
                    continue

                parent_node = parse_commit(parent_obj)
                parent_date_str = parent_node.date.split(' ')[0]

                if is_date_after(parent_date_str, start_date):
                    graph[parent_sha1] = parent_node

    return graph


def generate_plantuml(graph: Dict[str, CommitNode]) -> str:
    puml = "@startuml\n"
    puml += "digraph G {\n"
    puml += "  rankdir=BT;\n"
    puml += '  node [shape=box, style=filled, fillcolor="lightgreen"];\n'
    puml += '  edge [color="gray"];\n'

    for sha1, node in graph.items():
        message_label = node.message.replace('"', '\\"').replace('\n', '\\n').strip()
        label = f"{sha1[:7]}\\n{message_label}"
        puml += f'  "{sha1}" [label="{label}"];\n'

        for parent_sha1 in node.parents:
            if parent_sha1 in graph:
                puml += f'  "{parent_sha1}" -> "{sha1}";\n'

    puml += "}\n@enduml\n"
    return puml


def write_plantuml_file(plantuml_content: str, output_path: str) -> None:
    with open(output_path, 'w') as f:
        f.write(plantuml_content)


def main(config_path: str) -> None:
    config = parse_config(config_path)

    graph = build_commit_graph(config['repo_path'], config['start_date'])

    plantuml_content = generate_plantuml(graph)
    write_plantuml_file(plantuml_content, config['output_path'])

    print("PlantUML graph file generated successfully.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Git Commit Dependency Graph Visualizer')
    parser.add_argument('config_path', help='Path to the YAML configuration file')
    args = parser.parse_args()
    main(args.config_path)
