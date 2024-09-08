# Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
# Решение:
первый вариант: cut -d: -f1 /etc/passwd | sort

второй вариант: cat /etc/passwd | grep -Eo '^[^:]+' | sort
# Результат:
![image](https://github.com/user-attachments/assets/eda602f4-4450-4ba4-a745-0a9b72da63a9)

# Задача 2
![image](https://github.com/user-attachments/assets/2c68e73e-60f2-4b98-9192-5560f8ba4795)
# Решение
cat /etc/protocols | sort -k2 -n -r | head -n5 | awk '{print $2, $1}'
# Результат
![image](https://github.com/user-attachments/assets/13c44589-3631-401e-9d89-a58c519eb805)

# Задача 3
![image](https://github.com/user-attachments/assets/e0147872-f148-45b6-9815-c746a3f84f20)
# Решение
```py
s = input()
n = len(s)
print('+', end = '')
for _ in range(n + 2):
    print('-', end = '')
print('+', end = '')

print('\n| ' + s + ' |')

print('+', end = '')
for _ in range(n + 2):
    print('-', end = '')
print('+', end = '')
print()
```
python ./script.py

'michael'
# Результат
![image](https://github.com/user-attachments/assets/4fd6f611-414a-4368-92a9-1028aa9d5b9b)

# Задача 4
![image](https://github.com/user-attachments/assets/6c341119-5d8d-4eff-a9a9-43b3cde338a1)
# Решение
```py
filename = input("Enter an absolute file path:\n")
f = open(filename, 'r')
s = f.read()
res = []
idi = ''
for ch in s:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        idi += ch
    elif len(idi) > 0:
        if idi not in res:
            res.append(idi)
        idi = ''
print(*res)
```
python3 ./task_4.py

(C) Задача динамической связности в офлайне.cpp
# Результат
![image](https://github.com/user-attachments/assets/5c8bd403-6a85-400e-b755-aaeadb76c886)

# Задача 5
![image](https://github.com/user-attachments/assets/b868054b-12d8-4fc4-aa32-2ccf12e8eee4)
# Решение
```bash
#!/bin/bash

file=$1

# 755 - Чтение, запись, исполнение - Владалец | Чтение, исполнение - Другие пользователи
chmod 755 "./$file"

# Копируем команду в /usr/local/bin
sudo cp "$file" /usr/local/bin/
```
# Результат
![image](https://github.com/user-attachments/assets/4b676ea8-c4a3-4607-a270-082c3b6fd22d)

# Задача 6
![image](https://github.com/user-attachments/assets/ffa30588-5ca1-4cac-9664-492222248d93)
# Решение
```py
filename = input("Enter a file name:\n")
f = open(filename, 'r')
s = f.read()
if filename[-3:] == '.js' and s[1:3] == '//' or filename[-2:] == '.c' and s[1:3] == "//" or filename[-3:] == '.py' and s[0] == "#":
    print(f'{filename} has a leading comment')
else:
    print(f'{filename} does not have a leading comment')
```
# Результат
![image](https://github.com/user-attachments/assets/dd0b601a-4219-4267-9d07-bd5a33849204)
![image](https://github.com/user-attachments/assets/fc546b00-1365-43d8-9717-7e7132f8a412)

# Задача 7
![image](https://github.com/user-attachments/assets/db669673-0f05-47b7-9258-4f5aba4fbaee)
# Решение
```bash
#!/bin/bash

for file in "$@"; do
  # Проверка на наличие допустимого расширения
  if [[ "$file" =~ \.(c|js|py)$ ]]; then
    first_line=$(head -n 1 "$file")

    # Проверка на комментарий в первой строке для разных типов файлов
    if [[ "$file" =~ \.c$ && "$first_line" == "//"* ]] || \
       [[ "$file" =~ \.js$ && "$first_line" == "//"* ]] || \
       [[ "$file" =~ \.py$ && "$first_line" == "#"* ]]; then
      echo "$file has a comment in the first line."
    else
      echo "$file does not have a comment in the first line."
    fi
  fi
done
```
# Результат
![image](https://github.com/user-attachments/assets/41139c49-af96-4201-bac2-1da0d467fbb9)

# Задача 8
![image](https://github.com/user-attachments/assets/d4db55cf-3a52-430a-bae6-d5312c4dd595)
# Решение
```bash
#!/bin/bash

find . -name "*.$1" -print0 -maxdepth 1 | tar -czvf archive.tar.gz --null -T -
```
# Результат
![image](https://github.com/user-attachments/assets/89b45b3e-9a99-4571-908d-dbb04583701f)
![image](https://github.com/user-attachments/assets/8d62ed6e-95d7-48d1-a3d9-74f3ad0329a3)

# Задача 9
![image](https://github.com/user-attachments/assets/77c112f0-b197-446f-93f1-e133712d4d8b)
# Решение
```bash
#!/bin/bash

sed 's/    /\t/g' "$1" > "$2"
```
# Результат
![image](https://github.com/user-attachments/assets/8602b01f-e5cb-44cf-a00c-a7f923001965)
![image](https://github.com/user-attachments/assets/a326a7e6-c595-45ca-8438-611cc617447d)

# Задача 10
![image](https://github.com/user-attachments/assets/202ae659-5594-4b9f-bb47-e0112fd4ea96)
# Решение
```bash
#!/bin/bash

find "$1" -type f -empty -name "*.txt"
```
# Результат
![image](https://github.com/user-attachments/assets/5304813b-aa16-4efe-b1cf-a55e576bfe26)