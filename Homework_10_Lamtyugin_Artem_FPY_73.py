documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Вольтская Татьяна Анатольевна'},
    {'type': 'birth certificates', 'number': 'IIIАМ234567', 'name': 'Клепиковская Екатерина Дмитриевна'},
    {'type': 'passport', 'number': '1811 238647', 'name': 'Сотников Даниил Владимирович'},
    {'type': 'passport', 'number': '2351 421345', 'name': 'Василий Евгеньевич Гупкин'},
    {'type': 'passport', 'number': '2234 834534', 'name': 'Геннадий Эшович Покемонов'},
    {'type': 'birth certificates', 'number': 'IIIАМ939383', 'name': 'Захаров Андрей Вячеславович'},
    {'type': 'birth certificates', 'number': 'IIIАМ124525', 'name': 'Симонов Евгений Алексеевич'},
    {'type': 'marriage certificates', 'number': 'IIIRМ344257', 'name': 'Соловьева Елена Анатольевна'},
    {'type': 'marriage certificates', 'number': 'IIIRМ564322', 'name': 'Перл Роман Александрович'}

]

directories = {
        '1': ['2207 876234', 'IIIАМ234567', '1811 2386477', '2351 421345'],
        '2': ['2234 834534', 'IIIАМ939383', 'IIIАМ123525'],
        '3': ['IIIRМ344257', 'IIIRМ564322'],
        '4': []
      }


def people(doc):
    result = f' - Документ не существует.'
    for document in documents:
        if doc in document.get('number'):
            result = f' - Владелец: {document.get("name")}'
    print(result)


def shelf(doc):
    result = f' - Документ не существует.'
    for shelf_number, doc_number_ in directories.items():
        if doc in doc_number_:
            result = f' - Полка №: {shelf_number}'
    print(result)


def list_doc(documents_):
    for doc in documents_:
        type_ = doc['type']
        number_ = doc['number']
        name_ = doc['name']
        print('- {0} -  {1} -  {2}'.format(type_, number_, name_))


def add_doc(doc_type_, doc_number_, doc_owner_, shelf_id_):
    if shelf_id_ not in directories:
        return f' - Полка №{shelf_id_} не существует.'
    new_doc = dict(type=doc_type_, number=doc_number_, name=doc_owner_)
    documents.append(new_doc)
    directories[shelf_id_] += [doc_number_]
    return ' - Документ успешно добавлен.'


def delete(doc_number_):
    initial_len = len(documents)
    for i, d in enumerate(documents):
        if d['number'] == doc_number_:
            documents.pop(i)
    if initial_len == len(documents):
        return ' - Документ не существует.'
    for key, value in directories.items():
        if doc_number_ in value:
            value.remove(doc_number_)
    return ' - Документ успешно удален.'


def move(doc_number_, shelf_id_):
    doc_existence = False
    if shelf_id_ not in directories:
        return f' - Полка №{shelf_id_} не существует.'
    for key, value in directories.items():
        if doc_number_ in value:
            doc_existence = True
            directories[shelf_id_] += [doc_number_]
            value.remove(doc_number_)
    if doc_existence:
        return ' - Документ успешно перемещен.'
    else:
        return ' - Документ не существует.'


def add_shelf():
    number = input(' - Введите номер новой полки: ')
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
        people(str(input(' - Введите номер документа: ')))
    elif choice == 'l':
        list_doc(documents)
    elif choice == 's':
        shelf(str(input(' - Введите номер документа: ')))
    elif choice == 'a':
        doc_type = input(' - Введите тип документа: ')
        doc_number = input(' - Введите номер документа: ')
        doc_owner = input(' - Введите имя владельца документа: ')
        directories_keys = []
        for key_, value_ in directories.items():
            directories_keys.append(key_)
        shelf_id = input(f' - Введит номер полки: {"; ".join(directories_keys)}: ')
        print(add_doc(doc_type, doc_number, doc_owner, shelf_id))
    elif choice == 'd':
        doc_number = input(' - Введите номер документа: ')
        print(delete(doc_number))
    elif choice == 'm':
        doc_number = input(' - Введите номер документа, который хотите переместить: ')
        shelf_id = input(' - Введит номер полки, на которую хотите переместить документ: ')
        print(move(doc_number, shelf_id))
    elif choice == 'as':
        print(add_shelf())
    elif choice == 'q':
        print(' - До скорой встречи!')
        break
    else:
        print(' - Неизвестная команда, попробуйте выбрать из списка:')
