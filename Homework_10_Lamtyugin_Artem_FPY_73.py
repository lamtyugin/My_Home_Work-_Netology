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


def people(doc):
    result = ' - Документ не существует.'
    for document in documents:
        if document["number"] == doc:
            result = f' - Владелец: {document["name"]}'
    print(result)


def shelf(doc):
    result = ' - Документ не существует.'
    for shelf_number, doc_number_ in directories.items():
        if doc in doc_number_:
            return f' - Полка №: {shelf_number}'
    print(result)


def list_doc(documents_):
    for doc in documents_:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')


def add_doc():
    doc_type = input(' - Введите тип документа: ')
    doc_number = input(' - Введите номер документа: ')
    doc_owner = input(' - Введите имя владельца документа: ')
    shelf_id = input(f' - Введит номер полки: {"; ".join(directories.keys())}: ')
    if shelf_id not in directories:
        return f' - Полка №{shelf_id} не существует.'
    new_doc = dict(type=doc_type, number=doc_number, name=doc_owner)
    documents.append(new_doc)
    directories[shelf_id] += [doc_number]
    return ' - Документ успешно добавлен.'


def delete():
    doc_number = input(' - Введите номер документа: ')
    initial_len = len(documents)
    for i, d in enumerate(documents):
        if d['number'] == doc_number:
            documents.pop(i)
    if initial_len == len(documents):
        return ' - Документ не существует.'
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
    return ' - Документ успешно удален.'


def move():
    doc_number = input(' - Введите номер документа, который хотите переместить: ')
    shelf_id = input(' - Введит номер полки, на которую хотите переместить документ: ')
    doc_existence = False
    if shelf_id not in directories:
        return f' - Полка №{shelf_id} не существует.'
    for key, value in directories.items():
        if doc_number in value:
            doc_existence = True
            directories[shelf_id] += [doc_number]
            value.remove(doc_number)
    if doc_existence:
        return ' - Документ успешно перемещен.'
    else:
        return ' - Документ не существует.'


def add_shelf():
    number = input(' - Введите номер новой полки: ')
    if number in directories:
        return f' - Полка с №{number} уже существует'
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
        people(input(' - Введите номер документа: '))
    elif choice == 'l':
        list_doc(documents)
    elif choice == 's':
        shelf(str(input(' - Введите номер документа: ')))
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
