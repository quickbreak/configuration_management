# Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

# Решение:
первый вариант: cut -d: -f1 /etc/passwd | sort

второй вариант: cat /etc/passwd | grep -Eo '^[^:]+' | sort

# Результат:
![image](https://github.com/user-attachments/assets/eda602f4-4450-4ba4-a745-0a9b72da63a9)

