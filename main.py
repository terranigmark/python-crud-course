import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    }
]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')


def list_clients():
    print('UID | Name | Company | Email | Position')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position'],))


def update_client(client_name):
    global clients

    for i in range(len(clients)):
        if client_name in clients[i].values():
            updated_client_data = _get_client_from_user()
            clients[i].update(updated_client_data)
        else:
            _client_not_found()


def delete_client(client_name):
    global clients

    for i in range(len(clients)):
        if client_name in clients[i].values():
            del clients[i]
            break
        else:
            _client_not_found()


def search_client(client_name):
    for i in range(len(clients)):
        if client_name in clients[i].values():
            print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = i,
            name = clients[i]['name'],
            company = clients[i]['company'],
            email = clients[i]['email'],
            position = clients[i]['position'],))


def _get_client_field(field_name, message='What is the client {}?: '):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }

    return client

def _get_client_name():
    client_name = None

    while not client_name:
        client_name =  input('What is the client name?: ')

        if client_name.lower() == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _client_not_found():
    return print('Client not found in client\'s list.')


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do?')
    print('[C]reate client')
    print('[L]ist  clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client\n')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = input('What is the client\'s name to be updated?: ')
        update_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print(f'The client {client_name} is in the client\'s list')
        else:
            _client_not_found()
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')