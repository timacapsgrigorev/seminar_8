import json


def txt_json(src_file: str = 'text.txt',
             out_file: str = 'text.json'):
    """Импорт данных из .txt в .json"""
    with open(src_file, 'r') as file:
        names = dict(map(lambda x: tuple(x.split()),
                         file.read().split('\n')))

    with open(out_file, 'w') as file:
        json.dump(names, file, indent=4)


def add_usrs_json(filename: str = 'users.json'):
    """Добавление пользователей в json файл."""
    while True:
        try:
            with open(filename, 'r') as src:
                data = json.load(src)
        except FileNotFoundError:
            data = {str(i): [] for i in range(1, 8)}

        name = input('Введите имя: ')
        user_id = input('Введите ваш id: ')
        level = input('Введите ваш уровень доступа: ')
        data[level].append({'name': name, 'id': user_id})

        with open(filename, 'w') as res:
            json.dump(data, res, indent=4)


def json_to_csv(src_file: str = 'users.json',
                out_file: str = 'users.csv'):
    """Перевод из формата json в csv."""
    with open(src_file, 'r') as src:
        data = json.load(src)

    with open(out_file, 'w') as res:
        res.write('id,level,name')
        for level, users_lst in data.items():
            for user in users_lst:
                res.write(f'\n{user["id"]},{level},{user["name"]}')


def csv_to_json(src_file: str = 'users.csv',
                out_file: str = 'users_1.json'):
    """Перевод из csv к json формату."""
    with open(src_file, 'r') as src:
        data = list(map(lambda x: x.split(','),
                        src.read().split('\n')))

    for i in range(1, len(data)):
        data[i][0] = data[i][0].zfill(10)
        data[i][2] = data[i][2].capitalize()

        user_id = data[i][0]
        name = data[i][2]
        data[i].append(hash(user_id + name))

    data = data[1::]

    data = [{'id': u_id, 'level': level, 'name': uname, 'hash': uhash}
            for u_id, level, uname, uhash in data]

    with open(out_file, 'w') as res:
        json.dump(data, res, indent=4)


def file_converter(input_file: str, output_file: str, input_format: str, output_format: str):
    """Конвертация файлов разных форматов."""
    if input_format == 'txt' and output_format == 'json':
        txt_json(input_file, output_file)
    elif input_format == 'json' and output_format == 'csv':
        json_to_csv(input_file, output_file)
    elif input_format == 'csv' and output_format == 'json':
        csv_to_json(input_file, output_file)
    else:
        print("Неподдерживаемая комбинация форматов.")


file_converter('input.txt', 'output.json', 'txt', 'json')
file_converter('input.json', 'output.csv', 'json', 'csv')
file_converter('input.csv', 'output.json', 'csv', 'json')
