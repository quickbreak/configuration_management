<h1 align="center">
  Инструмент для преобразования текста из входного формата в выходной
</h1>

## Пример работы программы
Текст в json-формате:
```
{
  "constant_a": 123,
  "constant_b": 321,
  "constant_s1": "hello ",
  "constant_s2": "world",
  "expression_add": "?[constant_a constant_b add]",
  "expression_concatenate": "?[constant_s1 constant_s2 concatenate]",
  "expression_max": "?[constant_a constant_b max]",
  "list": [1, 2, 3],
  "ordinary_line": "I am a line",
  "some_log_path": "./log/log.json",
  "dict in dict": {
    "key1": "value1",
    "key2": 2,
    "dict in dict in dict": {
      "key3": "value3",
      "constant_52": 34
    }
  }
}
```
Текст в выходном формате:
```
dict(
   global @"constant_a" = 123
   global @"constant_b" = 321
   global @"constant_s1" = @"hello "
   global @"constant_s2" = @"world"
   @"expression_add" = @"?[constant_a constant_b add]"
   @"expression_concatenate" = @"?[constant_s1 constant_s2 concatenate]"
   @"expression_max" = @"?[constant_a constant_b max]"
   @"list" = ({ 1, 2, 3 })
   @"ordinary_line" = @"I am a line"
   @"some_log_path" = @"./log/log.json"
   @"dict in dict" = dict(
      @"key1" = @"value1"
      @"key2" = 2
      @"dict in dict in dict" = dict(
         @"key3" = @"value3"
         global @"constant_52" = 34
      )
   )
   @"result for ?[constant_a constant_b add]" = 444
   @"result for ?[constant_s1 constant_s2 concatenate]" = @"hello world"
   @"result for ?[constant_a constant_b max]" = 321
)
```
# Инструкция по скачиванию и запуску проекта на вашей машине (Linux)
Откройте терминал или командную строку и выполните следующие команды...  
## 1. Установка Python:
Установить python с pip:
```
sudo apt update  
sudo apt install python3 python3-pip
```
## 2. Клонирование репозитория
Скачать репозиторий:
```
git clone https://github.com/quickbreak/configuration_management.git
```
Перейти в нужный каталог:
```
cd configuration_management/FileTranslator
```
## 3. Создание и активация виртуального окружения
Создать виртуальное окружение:
```
python -m venv venv
```
Активировать его:
```
source venv/bin/activate
```
## 4. Установка зависимостей
```
pip install -r requirements.txt
```
## 5. Запуск проекта
Преобразовать текста из json-формата в выходной:
```
python3 ./main.py
```
## 6. Запуск тестов
Запустить тестирование:
```
py.test -v test_package/translator_test.py
```
