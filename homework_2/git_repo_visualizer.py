import zlib
import yaml
from datetime import datetime, timezone, timedelta
from typing import Dict, List
import os
import re


class GitObject:
    def __init__(self, sha1: str, type_: str, content: bytes):
        self.sha1 = sha1
        self.type_ = type_
        self.content = content.decode('utf-8', errors='replace')


class CommitNode:
    def __init__(self, sha1: str, author: str, date: str, message: str, parents: List[str], files: str):
        self.sha1 = sha1
        self.author = author
        self.date = date
        self.message = message
        self.parents = parents
        self.files = files


def parse_config(config_path: str) -> Dict[str, str]:
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


def get_commit_object(repo_path: str, object_hash: str) -> GitObject:
    """Сформировать объект GitObject"""
    object_path = os.path.join(repo_path, '.git', 'objects', object_hash[:2], object_hash[2:])
    try:
        with open(object_path, 'rb') as f:
            compressed_content = f.read()
            decompressed_content = zlib.decompress(compressed_content)
        return GitObject(object_hash, 'commit', decompressed_content)
    except FileNotFoundError:
        return GitObject(object_hash, 'beliberda', "beliberda_content".encode('utf-8'))
    except Exception as e:
        raise Exception(f"{str(e)}")


def get_files_tree(repo_path: str, object_hash: str) -> str:
    """Достать файлы"""
    tree_files_path = os.path.join(repo_path, ".git", "objects", object_hash[:2], object_hash[2:])
    with open(tree_files_path, "rb") as tree_file:
        files_string = ""
        data = zlib.decompress(tree_file.read())
        pattern = rb'(?P<mode>\d{5,6})\s+(?P<filename>[^\x00]+)'
        result_files = re.findall(pattern, data)
        for i in range(len(result_files)):
            mode, filename = result_files[i]
            mode = mode.decode('utf-8')
            filename = filename.decode('utf-8')
            result_files[i] = (mode, filename)
            if len(mode) == 5:
                files_string += f'|| {filename}\\n'
        for mode, filename in result_files:
            if len(mode) == 6:
                files_string += f'> {filename}\\n'

    return files_string


def get_files_commit(repo_path: str, object_hash: str) -> str:
    """Достать файлы"""
    object_path = os.path.join(repo_path, '.git', 'objects', object_hash[:2], object_hash[2:])
    try:
        with open(object_path, 'rb') as f:
            compressed_content = f.read()
            decompressed_content = zlib.decompress(compressed_content)
            tree_hash = str(decompressed_content).split('\\n')[0]
            start_pos = tree_hash.find('tree') + 5
            tree_hash = tree_hash[start_pos:]
            return get_files_tree(repo_path, tree_hash)
    except Exception as e:
        raise Exception(f"Error: {str(e)}")


def parse_commit(repo_path: str, obj: GitObject) -> CommitNode:
    """Сформировать CommitNode"""
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
    return CommitNode(obj.sha1, author, date, message.strip(), parents, get_files_commit(repo_path, obj.sha1))


def is_date_after(date1: str, date2: str) -> bool:
    """Проверить, что дата коммита позже нужной"""
    y1, m1, d1 = map(int, date1.split('-'))
    y2, m2, d2 = map(int, date2.split('-'))

    if y1 != y2:
        return y1 > y2
    if m1 != m2:
        return m1 > m2
    return d1 > d2


def rec(commits: Dict[str, CommitNode], commit: CommitNode, start_date: str, repo_path: str):
    """Проверить дату коммита и, если подходит, добавить в список"""
    if is_date_after(commit.date.split(' ')[0], start_date):
        commits[commit.sha1] = commit  # кладём себя
        for parent in commit.parents:  # проверяем родителей
            parent_obj = get_commit_object(repo_path, parent)
            if parent_obj.type_ == 'commit':
                parent_commit = parse_commit(repo_path, parent_obj)
                rec(commits, parent_commit, start_date, repo_path)


def get_commits_after_date(repo_path: str, start_date: str) -> Dict[str, CommitNode]:
    """Получить список коммитов, сделанных после нужной даты"""
    commit_path = os.path.join(repo_path, '.git', 'refs', 'heads', 'main')
    with open(commit_path, 'r') as f:
        head = f.read().strip()

    commits = {}
    head_obj = get_commit_object(repo_path, head)
    if head_obj.type_ == 'commit':
        head_commit = parse_commit(repo_path, head_obj)
        rec(commits, head_commit, start_date, repo_path)
    else:
        print('ERROR: head not found')
        exit(-1)

    return commits


def generate_plantuml(graph: Dict[str, CommitNode]) -> str:
    """Сформировать содержимое puml-файла"""
    puml = "@startuml\n"
    puml += "digraph G {\n"
    puml += "  rankdir=BT;\n"
    puml += '  node [shape=box, style=filled, fillcolor="lightgreen"];\n'
    puml += '  edge [color="gray"];\n'

    for sha1, node in graph.items():
        message_label = node.message.replace('"', '\\"').replace('\n', '\\n').strip()
        label = f"{sha1[:7]}\\n{message_label}\\n{node.files}"
        puml += f'  "{sha1}" [label="{label}"];\n'

        for parent_sha1 in node.parents:
            if parent_sha1 in graph:
                puml += f'  "{parent_sha1}" -> "{sha1}";\n'

    puml += "}\n@enduml\n"
    # print(puml)
    return puml


def write_plantuml_file(plantuml_content: str, pumlfile_path: str) -> None:
    with open(pumlfile_path, 'w') as f:
        f.write(plantuml_content)
