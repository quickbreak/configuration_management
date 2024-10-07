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
int: mCount = 6;
int: dCount = 5;
int: iCount = 2;
var 1..mCount: m;
var 1..dCount: d;
var 1..iCount: i;

array[1..mCount] of tuple(int, int, int): mVersions = 
  [(1,0,0), (1,1,0), (1,2,0), (1,3,0), (1,4,0), (1,5,0)];
array[1..dCount] of tuple(int, int, int): dVersions = 
  [(1,8,0), (2,0,0), (2,1,0), (2,2,0), (2,3,0)];
array[1..iCount] of tuple(int, int, int): iVersions = 
  [(1,0,0), (2,0,0)];

constraint (mVersions[m] == (1,0,0) \/ mVersions[m] == (1, 5, 0) /\ iVersions[i] == (1, 0, 0));
constraint (mVersions[m].2 >= 1 /\ mVersions[m].2 <= 5) -> (dVersions[d] == (2, 3, 0) \/ dVersions[d] == (2, 0, 0));
constraint mVersions[m] == (1, 0, 0) -> dVersions[d] == (1, 8, 0);
constraint (dVersions[d].2 >= 0 /\ dVersions[d].2 <= 3) -> iVersions[i] == (2, 0, 0);

solve satisfy;

output [
  "Menu version: ", show(mVersions[m]), "\n",
  "Dropdown version: ", show(dVersions[d]), "\n",
  "Icon version: ", show(iVersions[i]), "\n"
];
```
# Результат:
![image](https://github.com/user-attachments/assets/2000b7f1-cb70-4ab4-942e-7e9d510ecfea)
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
 enum Package = {
  root_1_0_0,

  foo_1_1_0,
  foo_1_0_0,

  left_1_0_0,
  right_1_0_0,

  shared_2_0_0,
  shared_1_0_0,

  target_2_0_0,
  target_1_0_0,
};

int: n = 7;

array[1..n] of set of Package: targets = [
  % Deps of root 1.0.0
  1: { foo_1_1_0, foo_1_0_0 },
  2: { target_2_0_0 },

  % Deps of foo 1.1.0
  3: { left_1_0_0 },
  4: { right_1_0_0 },

  % Deps of left 1.0.0
  5: { shared_1_0_0, shared_2_0_0 },

  % Deps of right 1.0.0
  6: { shared_1_0_0 },

  % Deps of shared 1.0.0
  7: { target_1_0_0 },
];

% set points to targets array
array[Package] of set of 1..n: dependencies = [
  root_1_0_0: { 1, 2 },
  foo_1_1_0: { 3, 4 },
  left_1_0_0: { 5 },
  right_1_0_0: { 6 },
  shared_1_0_0: { 7 },

  foo_1_0_0: { },
  shared_2_0_0: { },

  target_2_0_0: { },
  target_1_0_0: { },
];

array[Package] of var opt (1..100): install_order;

constraint occurs(install_order[root_1_0_0]);

constraint forall(p in Package where occurs(install_order[p])) (
  forall(dep in dependencies[p]) (
    exists(t in targets[dep]) (
      occurs(install_order[t]) /\
      install_order[t] < install_order[p]
    )
  )
);

output [
  if fix(occurs(install_order[p]))
  then "\(p): \(install_order[p])\n"
  else ""
  endif | p in Package
];
```
# Результат:
![image](https://github.com/user-attachments/assets/43fed2ba-ba99-48c1-8d17-d046aae23a30)

