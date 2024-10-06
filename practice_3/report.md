# Задача 1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
# Решение:
```
local groupPrefix = 'ИКБО-';
local year = '-20';
local groupNum = std.range(1, 24);

local studentData = [
  {name: "Иванов И.И.", age: 19, groupIndex: 4},
  {name: "Петров П.П.", age: 18, groupIndex: 5},
  {name: "Сидоров С.С.", age: 18, groupIndex: 5},
  {name: "Лермонтов М.Ю.", age: 120, groupIndex: 10}
];

{
  groups: [groupPrefix + std.toString(i) + year for i in groupNum],

  students: [
    {
      age: student.age,
      group: groupPrefix + std.toString(student.groupIndex) + year,
      name: student.name
    } for student in studentData
  ],

  subject: "Конфигурационное управление"
}
```
# Результат:
```
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 120,
      "group": "ИКБО-10-20",
      "name": "Лермонтов М.Ю."
    }
  ],
  "subject": "Конфигурационное управление"
}
```
# Задача 2
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
# Решение:
```
let Group = Text
let Student = { age : Natural, group : Group, name : Text }

let createGroup : Natural -> Text =
      λ(n : Natural) → "ИКБО-" ++ Natural/show n ++ "-23"

let groups : List Text =
      [ createGroup 1
      , createGroup 2
      , createGroup 3
      , createGroup 4
      , createGroup 5
      , createGroup 6
      , createGroup 7
      , createGroup 8
      , createGroup 9
      , createGroup 10
      ]

let createStudent : Natural -> Group -> Text -> Student =
      λ(age : Natural) →
      λ(group : Group) →
      λ(name : Text) →
        { age = age, group = group, name = name }

let students : List Student =
  [ createStudent 20 (createGroup 2) "Жагло И. Д."
  , createStudent 21 (createGroup 3) "Коротков А. А."
  , createStudent 22 (createGroup 1) "Запрягаев М. А."
  , createStudent 20 (createGroup 4) "Красоткин А. А."
  ]

in  { groups = groups, students = students, subject = "Программирование" }
```
# Результат:
```
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {"age": 19, "group": "ИКБО-4-20", "name": "Иванов И.И."},
    {"age": 18, "group": "ИКБО-5-20", "name": "Петров П.П."},
    {"age": 18, "group": "ИКБО-5-20", "name": "Сидоров С.С."},
    {"age": 120, "group": "ИКБО-10-20", "name": "Лермонтов М.Ю."}
  ],
  "subject": "Конфигурационное управление"
}
```
