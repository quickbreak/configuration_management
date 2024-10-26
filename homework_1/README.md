<h1 align="center">
  Эмулятор языка оболочки UNIX-подобной ОС
</h1>

## Пример работы программы
<div align="center">
  <img src="https://github.com/user-attachments/assets/236a9f75-ed48-4821-b943-c42d7c043a5f">
</div>

# Инструкция по скачиванию и запуску проекта на вашей машине
## 1. Установка Python:
Скачайте и установите Python с официального сайта, если Python ещё не установлен. Рекомендуемая версия — 3.8 или выше.
Во время установки выберите опцию Add Python to PATH.
## 2. Клонирование репозитория
Откройте терминал или командную строку и выполните следующие команды...  
Скачать репозиторий:
```
git clone https://github.com/quickbreak/configuration_management.git
```
Перейти в нужный каталог:
```
cd configuration_management/homework_1
```
## 3. Создание и активация виртуального окружения
Создать виртуальное окружение:
```
python -m venv venv
```
Активировать его
(Для Windows):
```
.\venv\Scripts\activate
```
(Для macOS/Linux):
```
source venv/bin/activate
```
## 4. Запуск проекта
```
python ./src/main.py ./config/config.json 
```
## 5. Запуск тестов
Перейти в каталог с тестами:
```
cd src
```
Запустить тестирование:
```
python -m unittest cmd_test.py
```
