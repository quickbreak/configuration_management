# Задача 2
![image](https://github.com/user-attachments/assets/2c68e73e-60f2-4b98-9192-5560f8ba4795)
# Решение
cat /etc/protocols | sort -k2 -n -r | head -n5 | awk '{print $2, $1}'
# Результат
![image](https://github.com/user-attachments/assets/13c44589-3631-401e-9d89-a58c519eb805)
