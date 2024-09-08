# Задача 4

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

