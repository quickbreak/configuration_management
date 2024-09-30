import zipfile


class Cmd:
    def __init__(self, filesystem_archive):
        self.arch = filesystem_archive
        self.current_path = zipfile.Path(self.arch)
        self.zip_path = str(self.current_path)[:-1]

    def __resolve(self, current_path, new_path='./') -> str:
        if new_path == '' or new_path == '.' or new_path == './':  # cwd
            return './'
        elif new_path[0] == '/':  # уже абсолютный путь
            return new_path[1:]
        # дан путь относительный,
        # формируем абсолютный путь без первого '/'
        addition = (str(current_path)
                    .replace(self.zip_path,
                             "/")[:-1]
                    .replace("//", "/"))
        if len(addition) > 0:
            addition = addition[1:]
        if len(new_path) > 1 and new_path[:2] == './':
            new_path = new_path[2:]
        if addition != '':
            return addition + '/' + new_path
        else:
            return new_path
        # elif new_path[0] not in './':
        #     return addition + new_path
        # elif len(new_path) > 2 and new_path[:3] == '../':

    def cd(self, new_path='./'):
        if new_path == "..":
            old_path = (str(self.current_path)
                        .replace(self.zip_path,
                                 "/")[:-1]
                        .replace("//", "/"))
            i = len(old_path) - 1
            while i >= 0 and old_path[i] != '/':
                old_path = old_path[:-1]
                i -= 1
            if i > 0:
                old_path = old_path[:-1]
            new_path = old_path

        new_path = self.__resolve(self.current_path, new_path)
        # print(self.arch.namelist())
        if new_path == './':
            return 0
        if new_path + '/' in self.arch.namelist() or new_path == '':
            self.current_path = zipfile.Path(self.arch)
            self.current_path = self.current_path.joinpath(new_path)
            return 0
        else:
            return 1

    def ls(self, file_path=''):
        old_path = (str(self.current_path)
                    .replace(self.zip_path,
                             "/")[:-1]
                    .replace("//", "/"))
        # ----------------------------------------------------------
        error = self.cd(file_path)
        res = []
        if error == 0:
            for i in self.current_path.iterdir():
                list_of = str(i)
                list_of = list_of.split('/')
                list_of = [x for x in list_of if len(x) > 0]
                res.append(list_of[-1])
            # ------------------------------------------------------
            self.cd(old_path)
            return res
        else:
            return 1

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
            if line_count > 0:
                memory += 1
            return [line_count, word_count, memory]
        else:
            i = len(file_path) - 1  # собираем имя файла
            file_name = ''
            while i >= 0 and file_path[i] != '/':
                file_name = file_path[i] + file_name
                i -= 1
            # собираем директорию
            # что если i == -1? то есть файл находится в текущей директории, путь до него относительный (path: file.txt)
            if i == -1:
                file_path = './'
            else:
                file_path = file_path[:i]
            old_path = (str(self.current_path)
                        .replace(self.zip_path,
                                 "/")[:-1]
                        .replace("//", "/"))
            # ----------------------------------------------------------
            error = self.cd(file_path)
            if error == 0:  # смогли поменять директорию
                new_path = (str(self.current_path)  # формируем текущее положение
                            .replace(self.zip_path,
                                     "/")[:-1]
                            .replace("//", "/"))
                if new_path != '/':
                    new_path = new_path[1:] + '/'
                if new_path + file_name in self.arch.namelist():  # такой файл есть в новой директории
                    with self.arch.open(new_path + file_name) as f:  # считаем
                        for line in f.readlines():
                            line_count += 1
                            word_count += len(line.split())
                            memory += len(line)
                        if line_count > 0:
                            memory += 1
                        self.cd(old_path)
                        return [line_count, word_count, memory]
                else:
                    self.cd(old_path)
                    return 1
                # ------------------------------------------------------
            else:
                return 1

    def find(self, dir_path='.', prototype=''):
        old_path = (str(self.current_path)
                    .replace(self.zip_path,
                             "/")[:-1]
                    .replace("//", "/"))
        # ----------------------------------------------------------
        error = self.cd(dir_path)
        res = []
        if error == 0:  # если перейти просили в директорию, и нам удалось
            for item in self.current_path.iterdir():
                item = str(item)
                extension = ''
                i = len(item) - 1
                while i > 0 and item[i] != '.':
                    i -= 1
                if item[i:] == prototype:
                    item = (item
                            .replace(self.zip_path,
                                     "/")
                            .replace("//", "/"))
                    res.append(item)
            # ------------------------------------------------------
            self.cd(old_path)
        return res
