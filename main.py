import csv
import os

filename = 'users.csv'


def create_file(filename):

    with open(filename, 'a') as f:
        collums = ["id", "nome", "email", "password"]
        writer = csv.DictWriter(f, fieldnames=collums)
        if not os.stat(filename).st_size:
            writer.writeheader()


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


def register_user(filename, **kwargs):
    with open(filename, 'a') as f:
        user = {'id': proximo_id(filename)}
        user.update(kwargs)

        collumns = ['id', 'nome', 'email', 'password']
        writer = csv.DictWriter(f, fieldnames=collumns)
        if not os.stat(filename).st_size:
            writer.writeheader()

        writer.writerow(user)

    return [user]


def login_required(func):
    def wrapper(*args):
        all = all_users(filename)
        for line in all[0]:
            if line['email'] == args[0] and line['password'] == args[1]:
                return func(*args)
        return "Usuário ou senha não autenticado corretamente"
    return wrapper


@login_required
def login_user(email, password):
    return "Usuário autenticado corretamente!"
