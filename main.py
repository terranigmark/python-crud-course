
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already in the client\'s list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        _client_not_found()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _client_not_found()


def search_client(client_name):
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do?')
    print('[C]reate client')
    print('[L]ist  clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_name():
    return input('What is the client name?: ')

def _client_not_found():
    return print('Client not found in client\'s list.')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the update client name?: ')
        update_client(client_name, updated_client_name)
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