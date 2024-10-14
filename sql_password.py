import re


def password_policy_check(username, password):

    regex = '^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{10,}$'

    if not re.match(regex, password):
        return "heslo je neplatné"

    if username in password:
        return "heslo obsahuje uzivatelske jmeno"


    for i in range(len(username) - 3):
        if username[i:i + 4] in password:
            return "Heslo nesmí obsahovat podřetězec username delší než 3 znaky."

    return "Heslo splňuje všechny požadavky."



username = "JanNovak"
password = "heSlo21Jan???"
result = password_policy_check(username, password)
print(result)