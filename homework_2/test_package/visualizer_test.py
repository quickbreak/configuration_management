import pytest
import git_repo_visualizer as visualizer


@pytest.fixture
def set_config():
    config = {
        'repo_path': "../../git-repo",
        'output_path': "./test_package/test_pumlfile.puml",
        'start_date': "2022-06-21"
    }
    return config


def test_parse_config(set_config):
    config = set_config
    assert visualizer.parse_config('./test_package/test_config.yaml') == config


def test_get_commits_after_date(set_config):
    config = set_config
    res = ['04fe0f38dc51783f43b35d3c63c007ee54cd7539',
           '0b2b417bdc0bdca5688bd39406b7b46a1ed62abf',
           'c3ec175c66b1dd5ec415e9dcab4c8598fc060103'
           ]
    got = visualizer.get_commits_after_date(config['repo_path'], config['start_date'])
    got = got.keys()
    ok = True
    for sha1 in res:
        if sha1 not in got:
            ok = False
    assert ok and len(got) == len(res)


def test_read_object(set_config):
    config = set_config
    obj = visualizer.get_commit_object(config['repo_path'], '04fe0f38dc51783f43b35d3c63c007ee54cd7539')
    assert obj.type_ == 'commit'
    assert 'author quickbreak' in obj.content


def test_parse_commit(set_config):
    config = set_config
    obj = visualizer.get_commit_object(config['repo_path'], '04fe0f38dc51783f43b35d3c63c007ee54cd7539')
    commit_node = visualizer.parse_commit(config['repo_path'], obj)
    assert commit_node.sha1 == '04fe0f38dc51783f43b35d3c63c007ee54cd7539'
    assert 'quickbreak' in commit_node.author
    assert commit_node.parents == ['c3ec175c66b1dd5ec415e9dcab4c8598fc060103']
    assert commit_node.message == 'next day commit'
    assert commit_node.date == '2024-10-26 13:22:57 +0300'


def test_is_date_after__year():
    assert visualizer.is_date_after("2023-01-01", "2022-01-01")


def test_is_date_after__month():
    assert visualizer.is_date_after("2023-02-01", "2023-01-01")


def test_is_date_after__day():
    assert visualizer.is_date_after("2023-01-02", "2023-01-01")


'''
def test_is_date_after__equal():    
    assert visualizer.is_date_after("2023-01-01", "2023-01-01")  # даты равны, результат False
'''


def test_build_commit_graph__full():
    assert len(visualizer.get_commits_after_date("../../git-repo", "2022-06-21")) == 3


def test_build_commit_graph__one():
    assert len(visualizer.get_commits_after_date("../../git-repo", "2024-10-25")) == 1


def test_generate_plantuml(set_config):
    config = set_config
    res = '@startuml\n\
digraph G {\n\
  rankdir=BT;\n\
  node [shape=box, style=filled, fillcolor="lightgreen"];\n\
  edge [color="gray"];\n\
  "04fe0f38dc51783f43b35d3c63c007ee54cd7539" [label="04fe0f3\\nnext day commit\\n> miha.txt\\n"];\n\
  "c3ec175c66b1dd5ec415e9dcab4c8598fc060103" -> "04fe0f38dc51783f43b35d3c63c007ee54cd7539";\n\
  "c3ec175c66b1dd5ec415e9dcab4c8598fc060103" [label="c3ec175\\nsecond line added\\n> miha.txt\\n"];\n\
  "0b2b417bdc0bdca5688bd39406b7b46a1ed62abf" -> "c3ec175c66b1dd5ec415e9dcab4c8598fc060103";\n\
  "0b2b417bdc0bdca5688bd39406b7b46a1ed62abf" [label="0b2b417\\nfirst commit: poetry in miha.txt\\n> miha.txt\\n"];\n\
}\n\
@enduml\n'
    # напоминание: понадобилось экранирование \n внутри одной строки res
    graph = visualizer.get_commits_after_date(config['repo_path'], config['start_date'])
    assert visualizer.generate_plantuml(graph) == res


def test_write_plantuml_file(set_config):
    config = set_config
    graph = visualizer.get_commits_after_date(config['repo_path'], config['start_date'])
    plantuml_content = visualizer.generate_plantuml(graph)
    visualizer.write_plantuml_file(plantuml_content, "./test_package/test_pumlfile.puml")
    with open("./test_package/test_pumlfile.puml", 'r') as f:
        content = f.read()
    assert content == plantuml_content


def test_miha_krasauchick():
    assert True
