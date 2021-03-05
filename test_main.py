from main import all_users, register_user, login_user


def test_all_users():
    FILENAME = 'users.csv'
    result = all_users(FILENAME)
    expect = ([], 0)

    assert result == expect


def test_register_user():
    FILENAME = 'users.csv'
    result = register_user(FILENAME, **{'nome': 'jose', 'email': "jose@hotmail.com", "password": '1234'})
    expect = [{'id': 5, 'nome': 'jose', 'email': 'jose@hotmail.com', 'password': '1234'}]

    assert result == expect


def test_login_user():
    result = login_user('jose@hotmail.com', '1234')
    expect = "Usuário autenticado corretamente!"

    assert result == expect
