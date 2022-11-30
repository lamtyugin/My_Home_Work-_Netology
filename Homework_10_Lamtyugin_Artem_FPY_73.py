documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():
    doc = input(' - Введите номер документа: ')
    result = ' - Документ не существует.'
    for document in documents:
        if document["number"] == doc:
            result = f' - Владелец: {document["name"]}'
            break
    return result


def shelf():
    doc = input(' - Введите номер документа: ')
    result = ' - Документ не существует.'
    for shelf_number, doc_number_ in directories.items():
        if doc in doc_number_:
            result = f' - Полка №: {shelf_number}'
            break
    return result


def list_documents():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def add_doc():
    document_type = input(' - Введите тип документа: ')
    document_number = input(' - Введите номер документа: ')
    document_owner = input(' - Введите имя владельца документа: ')
    shelf_id = input(f' - Введит номер полки: {"; ".join(directories.keys())}: ')
    if shelf_id not in directories:
        return f' - Полка №{shelf_id} не существует.'
    new_doc = dict(type=document_type, number=document_number, name=document_owner)
    documents.append(new_doc)
    directories[shelf_id] += [document_number]
    return ' - Документ успешно добавлен.'


def delete():
    number = input(' - Введите номер документа: ')
    initial_len = len(documents)
    for key, value in enumerate(documents):
        if value['number'] == number:
            documents.pop(key)
    if initial_len == len(documents):
        return ' - Документ не существует.'
    for key, value in directories.items():
        if number in value:
            value.remove(number)
    return ' - Документ успешно удален.'


def move():
    document_number = input(' - Введите номер документа, который хотите переместить: ')
    shelf_id = input(' - Введит номер полки, на которую хотите переместить документ: ')
    document_existence = False
    if shelf_id not in directories:
        return f' - Полка №{shelf_id} не существует.'
    for key, value in directories.items():
        if document_number in value:
            document_existence = True
            directories[shelf_id] += [document_number]
            value.remove(document_number)
    if document_existence:
        return ' - Документ успешно перемещен.'
    else:
        return ' - Документ не существует.'


def add_shelf():
    number = input(' - Введите номер новой полки: ')
    if number in directories:
        return f' - Полка №{number} уже существует'
    else:
        directories[number] = []
        return f' - Полка №: {number} добавлена.'


while True:
    choice = input('\n- Какую операцию вы хотите выполнить?\n\n'
                   '- p: команда, по номеру документа выведет имя человека, которому он принадлежит\n'
                   '- l: команда, выведет список всех документов в установленном формате\n'
                   '- s: команда, по номеру документа выведет номер полки, на которой он находится\n'
                   '- a: команда, которая добавит новый документ в каталог и в перечень полок\n'
                   '- d: команда, которая удалит полностью документ из каталога и его номер из перечня полок\n'
                   '- m: команда, которая переместит документ с текущей полки на целевую\n'
                   '-as: команда, которая создания новой полки\n'
                   '- q: команда, для завершение работы\n').lower()
    if choice == 'p':
        print(people())
    elif choice == 'l':
        list_documents()
    elif choice == 's':
        print(shelf())
    elif choice == 'a':
        print(add_doc())
    elif choice == 'd':
        print(delete())
    elif choice == 'm':
        print(move())
    elif choice == 'as':
        print(add_shelf())
    elif choice == 'q':
        print(' - До скорой встречи!')
        break
    else:
        print(' - Неизвестная команда, попробуйте выбрать из списка:')
