# Задача 1
Вывести служебную информацию о пакете matplotlib (Python).
# Решение:
```
pip show matplotlib
```
# Результат:
![image](https://github.com/user-attachments/assets/f6112bed-f05a-43ee-b9d0-cbd67d827470)
![image](https://github.com/user-attachments/assets/1b0d992c-2cc3-465f-b5c5-aca950101331)
# Задача
Как получить пакет без менеджера пакетов, прямо из репозитория?
# Решение
git clone https://github.com/matplotlib/matplotlib.git
# Результат
![image](https://github.com/user-attachments/assets/16bdf2c9-110e-4d0f-b7a5-10bd5f240370)
# Задача 2
Вывести служебную информацию о пакете express (JavaScript).
# Решение:
```
npm info express
```
# Результат:
![image](https://github.com/user-attachments/assets/ac4329aa-5cf3-4d02-8ae6-6cdb51222b22)
# Задача
Как получить пакет без менеджера пакетов, прямо из репозитория?
# Решение
git clone https://github.com/expressjs/express.git
# Результат
![image](https://github.com/user-attachments/assets/7235cdab-fd8b-4e5b-9612-cec2b62b4a40)
# Задача 3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.
# Решение:
```
echo 'digraph { matplotlib -> contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, "python-dateutil" }' | dot -Tsvg > matplotlib.svg
echo 'digraph { express -> accepts, "array-flatten", "body-parser", "content-disposition", "content-type", "cookies-signature", cookie, debug, depd, encodeurl, "escape-html", etag, finalhandler, "..." }' | dot -Tsvg > express.svg
```
# Результат:
![image](https://github.com/user-attachments/assets/c678e661-91eb-4f13-b540-a23af767ba6f)
![image](https://github.com/user-attachments/assets/b0bdef68-99aa-4b07-9d01-fd800fbaa7b2)


