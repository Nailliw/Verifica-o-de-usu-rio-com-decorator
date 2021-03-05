import csv
import os


def create_file(filename):

    with open(filename, 'a') as f:
        collums = ["id", "nome", "email", "password"]
        writer = csv.DictWriter(f, fieldnames=collums)
        if not os.stat(filename).st_size:
            writer.writeheader()


filename = 'users.csv'


def proximo_id(filename):
    id = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            id.append(int(line['id']))

    return sorted(id)[-1]+1 if id != [] else 1


def all_users(filename):
    characters = []
    id = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            characters.append(line)
            id.append(int(line['id']))

    if id == []:
        return (characters, 0)
    if id != []:
        return (characters, id[-1])


todos = all_users(filename)


def register_user(filename, **kwargs):
    with open(filename, 'a') as f:
        id = {'id': proximo_id(filename)}
        id.update(kwargs)

        collumns = ['id', 'nome', 'email', 'password']
        writer = csv.DictWriter(f, fieldnames=collumns)
        if not os.stat(filename).st_size:
            writer.writeheader()

        writer.writerow(id)

    return id


user_registered = register_user(filename, **{'nome': 'jose', 'email': "jose@hotmail.com", "password": '1234'})
print(user_registered)


def login_required(func):
    def wrapper(email, password):
        pass


def login_user(email, password):
    pass


user = login_user('jose@hotmail.com', '1234')
print(user)
