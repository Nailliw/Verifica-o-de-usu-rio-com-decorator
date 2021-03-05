import csv
import os


def create_file(filename):

    with open(filename, 'a') as f:
        collums  = ["id", "nome", "email", "password"]
        writer = csv.DictWriter(f, fieldnames=collums )
        if not os.stat(filename).st_size:
            writer.writeheader()


filename = 'users.csv'
create_file(filename)


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
print(todos)

