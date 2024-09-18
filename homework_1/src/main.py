import zipfile
import json
import argparse
import datetime

from Cmd import Cmd

# main:
parser = argparse.ArgumentParser()
parser.add_argument("config_path", help="use path to add the configuration",
                    type=str)
parser.add_argument("--script", help="run commands from the script file",
                    type=str, default=None)
args = parser.parse_args()

# Чтение файла конфигурации
with open(args.config_path, 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

username = config['username']
hostname = config['hostname']
zip_path = config['zip_path']
log_path = config['log_path']
start_script_path = config['start_script_path']  # зачем?

with zipfile.ZipFile(zip_path, 'r') as arch:
    manipulator = Cmd(arch)

    records = []
    log_file = open(log_path, "w", encoding="UTF-8")
    tick = 0
    if args.script is not None:
        script_file = open(start_script_path, 'r', encoding="UTF-8")
    while True:
        current_path = (str(manipulator.current_path)
                        .replace("D:/micha/Учёба -- пары/3 Семестр/configuration_management/homework_1/archive.zip",
                                 "/")[:-1]
                        .replace("//", "/"))
        if args.script is None:
            command = input(f'{username}@{hostname}:{current_path}$ ')
        else:
            command = script_file.readline()
        records.append({"username": username,
                "date": "",
                "time": "",
                "command": ""
                })
        records[tick]["command"] = command

        command = command.strip().split()
        if len(command) == 0:
            continue
        if command[0] == 'exit':
            break
        elif command[0] == 'ls':
            if len(command) == 1:
                manipulator.ls()
            else:
                manipulator.ls(command[1])
        elif command[0] == 'cd':
            manipulator.cd(command[1])
        elif command[0] == 'wc':
            if len(command) == 1:
                manipulator.wc()
            else:
                manipulator.wc(command[1])
        elif command[0] == 'find':
            if len(command) == 1:
                manipulator.find()
            else:
                manipulator.find(command[1])
        else:
            print('unsupported command')

        records[tick]['date'] = str(datetime.date.today())
        records[tick]['time'] = str(datetime.datetime.now().time())[:8]
        tick += 1
    json.dump(records, log_file, ensure_ascii=False, indent=2)

'''
добавить --script
тестирование
команда find
'''