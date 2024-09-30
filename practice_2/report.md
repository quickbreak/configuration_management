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
# Задача 4
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.
# Решение:
```
include "globals.mzn";
array[1..6] of var 0..9: digits;
constraint sum(digits[1..3]) = sum(digits[4..6]);
constraint all_different(digits);
solve minimize sum(digits[1..3]);
output ["digits: \(digits)"];
```
# Результат:
![image](https://github.com/user-attachments/assets/f8c0e781-0bc3-40f7-ba33-bee314765d50)
# Задача 5
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.
![image](https://github.com/user-attachments/assets/5d054df5-730c-4a3b-84f5-52be5357aa2e)
# Решение:
```
% Определяем пакеты
  enum PACKAGES = {
      root, 
      menu_1_0_0, menu_1_1_0, menu_1_2_0, menu_1_3_0, menu_1_4_0, menu_1_5_0, 
      dropdown_2_0_0, dropdown_2_1_0, dropdown_2_2_0, dropdown_2_3_0, dropdown_1_8_0,
      icons_1_0_0, icons_2_0_0
  };
  
  % Переменные, указывающие, установлен ли пакет (1) или нет (0)
  array[PACKAGES] of var 0..1: installed;
  
  % Обязательно устанавливаем root
  constraint
      installed[root] == 1;
  
  % Ограничения зависимостей
  constraint
      (installed[root] == 1) -> (installed[menu_1_0_0] == 1 /\ installed[menu_1_5_0] == 1 /\ installed[icons_1_0_0] == 1) /\
      (installed[menu_1_5_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_4_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_3_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_2_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_1_0] == 1) -> (installed[dropdown_2_3_0] == 1 /\ installed[dropdown_2_0_0] == 1) /\
      (installed[menu_1_0_0] == 1) -> (installed[dropdown_1_8_0] == 1) /\
      (installed[dropdown_2_0_0] == 1) -> (installed[icons_2_0_0] == 1) /\
      (installed[dropdown_2_1_0] == 1) -> (installed[icons_2_0_0] == 1) /\
      (installed[dropdown_2_2_0] == 1) -> (installed[icons_2_0_0] == 1) /\
      (installed[dropdown_2_3_0] == 1) -> (installed[icons_2_0_0] == 1);
  
  % Целевая функция: минимизируем количество установленных пакетов
  solve minimize sum(installed);
  
  % Выводим результат
  output [
      "Installed packages: ", show(installed)
  ];
```
# Результат:
![image](https://github.com/user-attachments/assets/84ddad03-ee66-4a99-9c51-d042d9e1f623)
# Задача 6
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:
'''
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
'''
# Решение:
```
 % Определяем пакеты
  enum PACKAGES = {
      root, 
      foo_1_0_0, foo_1_1_0, 
      left_1_0_0, right_1_0_0, 
      shared_1_0_0, shared_2_0_0, 
      target_1_0_0, target_2_0_0
  };
  
  % Переменные, указывающие, установлен ли пакет (1) или нет (0)
  array[PACKAGES] of var 0..1: installed;
  
  % Ограничения зависимостей
  constraint
      (installed[root] == 1) -> (installed[foo_1_1_0] == 1 /\ installed[target_2_0_0] == 1) /\
      (installed[foo_1_1_0] == 1) -> (installed[left_1_0_0] == 1 /\ installed[right_1_0_0] == 1) /\
      (installed[left_1_0_0] == 1) -> (installed[shared_1_0_0] == 1) /\
      (installed[right_1_0_0] == 1) -> (installed[shared_2_0_0] == 1) /\ (installed[shared_1_0_0] == 0) /\
      (installed[shared_1_0_0] == 1) -> (installed[target_1_0_0] == 1);
  
  % Обязательно устанавливаем root
  constraint
      installed[root] == 1;
  
  % Целевая функция: минимизируем количество установленных пакетов
  solve minimize sum(installed);
  
  % Выводим результат
  output [
      "Installed packages: ", show(installed)
  ];
```
# Результат:
![image](https://github.com/user-attachments/assets/33649ed8-8c5a-4978-8fe0-62fb87f9cb38)
