from operator import itemgetter


class File:
    def __init__(self, id, name, size, dir_id):
        self.id = id
        self.name = name
        self.size = size
        self.dir_id = dir_id


class Dir:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FileDir:
    def __init__(self, dir_id, file_id):
        self.dir_id = dir_id
        self.file_id = file_id


dirs = [
    Dir(1, 'Архив'),
    Dir(2, 'Документы'),
    Dir(3, 'Анализ'),
    Dir(4, 'Музыка'),
]

files = [
    File(1, 'Отчет.docx', 250, 2),
    File(2, 'Резервная_копия.zip', 5000, 1),
    File(3, 'Данные.csv', 1200, 3),
    File(4, 'Песня.mp3', 4500, 4),
    File(5, 'Заметки.txt', 15, 2),
    File(6, 'Старый_архив.zip', 3000, 1),
]

files_dirs = [
    FileDir(1, 2),
    FileDir(1, 6),
    FileDir(2, 1),
    FileDir(2, 5),
    FileDir(3, 3),
    FileDir(4, 4),
    FileDir(3, 1),
]


def main():
    one_to_many = [(f.name, f.size, d.name)
                   for d in dirs
                   for f in files
                   if f.dir_id == d.id]

    many_to_many_temp = [(d.name, fd.dir_id, fd.file_id)
                         for d in dirs
                         for fd in files_dirs
                         if d.id == fd.dir_id]

    many_to_many = [(f.name, f.size, dir_name)
                    for dir_name, dir_id, file_id in many_to_many_temp
                    for f in files
                    if f.id == file_id]

    print('Задание Г1 (один-ко-многим)')
    print('Список каталогов, название которых начинается с буквы "А", и файлы в них:')
    res_1 = {d.name: [name for name, _, dname in one_to_many if dname == d.name]
             for d in dirs if d.name.startswith('А')}
    print(res_1)

    print('\nЗадание Г2 (один-ко-многим)')
    print('Список каталогов с максимальным размером файла в каждом каталоге, '
          'отсортированный по максимальному размеру:')
    res_2_unsorted = []
    for d in dirs:
        d_files = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_files) > 0:
            d_sizes = [size for _, size, _ in d_files]
            res_2_unsorted.append((d.name, max(d_sizes)))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(res_2)

    print('\nЗадание Г3 (многие-ко-многим)')
    print('Список всех связанных файлов и каталогов, отсортированный по каталогам:')
    res_3 = sorted(many_to_many, key=itemgetter(2))
    print(res_3)


if __name__ == '__main__':
    main()
