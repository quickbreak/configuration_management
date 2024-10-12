import zipfile
import json
import argparse
import datetime

from Cmd import Cmd

# main:
parser = argparse.ArgumentParser()
parser.add_argument("config_path", help="use path to add the configuration",
                    type=str)
parser.add_argument("--script", action='store_true', help="executes commands automatically")

args = parser.parse_args()

# Чтение файла конфигурации
with open(args.config_path, 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

username = config['username']
hostname = config['hostname']
zip_path = config['zip_path']
log_path = config['log_path']
start_script_path = config['start_script_path']

with zipfile.ZipFile(zip_path, 'r') as arch:
    manipulator = Cmd(arch)

    records = []
    log_file = open(log_path, "w", encoding="UTF-8")
    tick = 0
    if args.script:
        script_file = open(start_script_path, 'r', encoding="UTF-8")
    while True:
        current_path = (str(manipulator.current_path)
                        .replace(zip_path,
                                 "/")[:-1]
                        .replace("//", "/"))
        if not args.script:
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
        # logging --------------------------------------------
        records[tick]['date'] = str(datetime.date.today())
        records[tick]['time'] = str(datetime.datetime.now().time())[:8]
        tick += 1
        # ----------------------------------------------------
        if len(command) == 0:
            continue
        if command[0] == 'exit':
            break
        elif command[0] == 'pwd':
            print(current_path)
        elif command[0] == 'ls':
            res = []
            if len(command) == 1:
                res = manipulator.ls()
            else:
                res = manipulator.ls(command[1])

            if res == 1:
                print("No such file or directory")
            else:
                for item in res:
                    print(item, end=' ')
                if len(res) > 0:
                    print()
        elif command[0] == 'cd' and len(command) == 2:
            res = manipulator.cd(command[1])
            if res == 1:
                print("No such file or directory")
        elif command[0] == 'wc':
            if len(command) == 1:
                res = manipulator.wc()
            else:
                res = manipulator.wc(command[1])

            if res == 1:
                print('No such file or directory')
            else:
                line_count = res[0]
                word_count = res[1]
                memory = res[2]
                print(f'        {line_count}       {word_count}       {memory}')
        elif command[0] == 'find':
            res = []
            if len(command) == 2:
                res = manipulator.find('', command[1])
            elif len(command) == 3:
                res = manipulator.find(command[1], command[2])
            for item in res:
                print(item)
        else:
            print('unsupported command')
    json.dump(records, log_file, ensure_ascii=False, indent=2)
