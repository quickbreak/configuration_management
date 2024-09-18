import zipfile


class Cmd:
    def __init__(self, filesystem_archive):
        self.arch = filesystem_archive
        self.current_path = zipfile.Path(self.arch)

    @staticmethod
    def resolve(current_path, new_path='./') -> str:
        if new_path == '':
            return ''
        if new_path == '.':  # cwd
            path = './'
        if new_path[0] == '/':  # уже абсолютный путь
            return new_path[1:]
        addition = (str(current_path)
                    .replace("D:/micha/Учёба -- пары/3 Семестр/configuration_management/homework_1/archive.zip",
                             "/")[:-1]
                    .replace("//", "/"))
        if addition != '/':
            addition = addition[1:] + '/'
        else:
            addition = ''
        if len(new_path) > 1 and new_path[:2] == './':  # относительный путь
            return addition + new_path[2:]
        elif new_path[0] not in './':  # относительный путь
            return addition + new_path
        # elif len(new_path) > 2 and new_path[:3] == '../':

    def cd(self, new_path='./'):
        new_path = self.resolve(self.current_path, new_path)
        if new_path + '/' in self.arch.namelist() or new_path == '':
            self.current_path = zipfile.Path(self.arch)
            self.current_path = self.current_path.joinpath(new_path)
            return 0
        else:
            print("No such file or directory")
            return 1

    def ls(self, file_path='./'):
        old_path = (str(self.current_path)
                    .replace("D:/micha/Учёба -- пары/3 Семестр/configuration_management/homework_1/archive.zip",
                             "/")[:-1]
                    .replace("//", "/"))
        if old_path != '/':
            old_path = old_path[1:] + '/'
        else:
            old_path = ''
        # ----------------------------------------------------------
        error = self.cd(file_path)
        if error == 0:
            empty = True
            for i in self.current_path.iterdir():
                empty = False
                list_of = str(i)
                list_of = list_of.split('/')
                list_of = [x for x in list_of if len(x) > 0]
                print(list_of[-1], end=" ")
            if not empty:
                print()
            # ------------------------------------------------------
            self.cd(old_path)

    def wc(self, file_path=''):
        line_count = 0
        word_count = 0
        memory = 0
        if file_path == '':
            while True:
                line = input()
                if line == 'eof':
                    break
                line_count += 1
                word_count += len(line.split())
                memory += len(line)
            print(f'        {line_count}       {word_count}       {memory + 1}')
        else:
            i = len(file_path) - 1
            file_name = ''
            while i >= 0 and file_path[i] != '/':
                file_name = file_path[i] + file_name
                i -= 1
            file_path = file_path[:i]  # что если i == -1?
            old_path = (str(self.current_path)
                        .replace("D:/micha/Учёба -- пары/3 Семестр/configuration_management/homework_1/archive.zip",
                                 "/")[:-1]
                        .replace("//", "/"))
            if old_path != '/':
                old_path = old_path[1:] + '/'
            else:
                old_path = ''
            # ----------------------------------------------------------
            error = self.cd(file_path)
            if error == 0:  # смогли поменять директорию
                new_path = (str(self.current_path)  # формируем текущее положение
                            .replace("D:/micha/Учёба -- пары/3 Семестр/configuration_management/homework_1/archive.zip",
                                     "/")[:-1]
                            .replace("//", "/"))
                if new_path != '/':
                    new_path = new_path[1:] + '/'
                else:
                    new_path = ''
                if new_path + file_name in self.arch.namelist():  # такой файл есть в новой директории
                    with self.arch.open(new_path + file_name) as f:  # считаем
                        for line in f.readlines():
                            line_count += 1
                            word_count += len(line.split())
                            memory += len(line)
                        print(f'        {line_count}       {word_count}       {memory + 1}')
                else:
                    print("No such file or directory")
                # ------------------------------------------------------
                self.cd(old_path)

    def find(self, dir_path=''):
        print('unsupported command')
