# Практическое задание №4. Системы контроля версий
## Задача 1
### Условие:
![image](https://github.com/user-attachments/assets/52fb082b-5f2d-46be-b0d3-9383b59afc93)
### Решение:
```
git commit
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout [in_hash]
git tag in 
```
### Результат
![result_image](https://github.com/user-attachments/assets/2bd68362-e487-4ec9-b27b-9fb1bbea2f27)
## Задача 2
### Условие:
Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.
### Решение и результат:
![image](https://github.com/user-attachments/assets/e8fbb029-93b0-4506-893b-ad527cec7f52)
## Задача 3
### Условие:
Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.  

Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.  

Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.  

Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.  

Прислать список набранных команд и содержимое git log.
### Решение:
```
mkdir server && cd server
git init --bare

cd ../conf-uprav_prac-4
git remote add origin ../server
git push origin main

cd ../
git clone ./server/ copyserver && cd copyserver
git config user.name coder2
git config user.email coder2@yandex.ru
touch readme.md
echo "coder2 first line" > readme.md
git add readme.md
git commit -m "coder2: copyserver first commit"
git push origin main

cd ../conf-uprav_prac-4
git pull origin main
echo "michaelcoder(coder1) first line" >> readme.md
git add readme.md
git commit -m "michaelcoder(coder1) second commit"
git push origin main

cd ../copyserver
echo "coder2 second line" >> readme.md
git add readme.md
git commit -m "coder2 second commit"

git push origin main [failed]
git pull origin main
code readme.md
[Accept both...]
git add readme.md
git commit -m "Resolve merge conflict by incorporating both suggestions"
git push origin main
```
### Результат
![image](https://github.com/user-attachments/assets/01159d3e-7580-4db8-9a2d-29b07936e56b)

## Задача 4
### Условие:
Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.
### Решение:
```
import os
import subprocess

def get_type_content(repo_path: str, sha1: str):

    result = subprocess.run(
        ['git', 'cat-file', '-p', sha1],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    content = ""
    if result.returncode != 0:
        raise FileNotFoundError(f"Object '{sha1}' not found.")
    else:
        content = result.stdout.encode('utf-8').decode('utf-8', errors='replace')

    # Determine the type of the object
    type_result = subprocess.run(
        ['git', 'cat-file', '-t', sha1],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    obj_type = type_result.stdout.strip()

    return [obj_type, content]



def get_parents(content):
    if content == "":
        return ""
    lines = content.split('\n')
    parents = []
    for line in lines:
        if line.startswith('parent '):
            parents.append(line[7:])
    return (parents)


def print_all(repo_path: str):
    lst = []
    path = repo_path + '/.git/objects'
    lst = os.listdir(path)
    while len(lst) > 0:
        dr = lst.pop()
        if dr in {'info', 'pack'}:
            continue

        file_name = os.listdir(f'{path}/{dr}')[0]
        sha1 = dr + file_name
        # print(sha1)
        res = get_type_content(repo_path, sha1)
        content = res[0], res[1]
        print(content)
        print('-' * 100)
```
### Результат
```
print_all("../../copyserver")
```
![image](https://github.com/user-attachments/assets/1225b9f5-312c-4411-972a-2daee3919a78)

