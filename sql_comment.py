def create_insert_query(nickname, text):
    nickname = nickname.replace("'", "''")
    nickname = nickname.replace('\\', '\\\\')
    nickname = nickname.replace('"', '\\"')


    text = text.replace("'", "''")
    text = text.replace('\\', '\\\\')
    text = text.replace('"', '\\"')

    query = f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{nickname}', '{text}')"

    return query



author = "JanNovak"
message = "ahoj ahoj ahoj"
sql_query = create_insert_query(author, message)
print(sql_query)