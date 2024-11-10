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

### Решение:
```
 
```
### Результат
