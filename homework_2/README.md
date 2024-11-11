<h1 align="center">
  Визуализатор истории коммитов гит-репозитория
</h1>

## Пример работы программы
<div align="center">
  <img src="https://github.com/user-attachments/assets/e9d17151-191b-468d-9938-e67f4785d72d">
</div>

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
cd configuration_management/homework_2
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
sudo apt install plantuml
pip install -r requirements.txt
```
## 5. Запуск проекта
Визуализировать историю коммитов гит-репозитория:
```
python3 ./main.py ./config.yaml
```
Результат будет сохранён в файл pumlfile.png
## 6. Запуск тестов
Запустить тестирование:
```
py.test -v test_package/visualizer_test.py
```
