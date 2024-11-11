import git_repo_visualizer as visualizer
import argparse
import subprocess


def main(config_path: str) -> None:
    config = visualizer.parse_config(config_path)

    graph = visualizer.get_commits_after_date(config['repo_path'], config['start_date'])

    plantuml_content = visualizer.generate_plantuml(graph)
    visualizer.write_plantuml_file(plantuml_content, config['pumlfile_path'])

    print("PlantUML graph file generated successfully")

    subprocess.run(['plantuml', config['pumlfile_path']])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Git Commit Dependency Graph Visualizer')
    parser.add_argument('config_path', help='Path to the YAML configuration file')
    args = parser.parse_args()
    main(args.config_path)
