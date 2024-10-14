import re

def create_insert_query(nickname, tel_number):
    nickname = nickname.replace("'", "''")
    nickname = nickname.replace('\\', '\\\\')
    nickname = nickname.replace('"', '\\"')


    tel_number = tel_number.replace("'", "''")
    tel_number = tel_number.replace('\\', '\\\\')
    tel_number = tel_number.replace('"', '\\"')

    query = f"UPDATE USER SET PHONE = '{tel_number}' WHERE USERNAME = '{nickname}')"

    return query

def is_nine_digit_number(tel_number):
    # Kontrola, zda je vstupní hodnota číslo s 9 číslicemi
    pattern = '^\d{9}$'
    return bool(re.match(pattern, tel_number))



author = "JanNovak"
tel_number = "123456784"

if is_nine_digit_number(tel_number):
    sql_query = create_insert_query(author, tel_number)
    print(sql_query)

else:
    print(f"{tel_number} není platné číslo s 9 číslicemi.")
