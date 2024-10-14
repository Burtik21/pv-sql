import re

def create_insert_query(nickname, text):
    # Nahrazení znaků pro SQL
    nickname = nickname.replace("'", "''")
    nickname = nickname.replace('\\', '\\\\')
    nickname = nickname.replace('"', '\\"')

    # Vytvoření regexu pro cenzuru jmen
    pattern = r'\b(?:Ondřej Mandík|Ondra Mandík|Alena Reichlová(?:ová|é)?|Jára Cimrman(?:em|ovi|u|a)?|Jára|Petr Novák|Petr|Petrův|Marie Nováková|Maruška)\b'

    # Nahrazení jmen textem [AUTOMATICKY CENZUROVÁNO]
    text = re.sub(pattern, '[AUTOMATICKY CENZUROVÁNO]', text, flags=re.IGNORECASE)

    # Nahrazení znaků pro SQL
    text = text.replace("'", "''")
    text = text.replace('\\', '\\\\')
    text = text.replace('"', '\\"')

    # Vytvoření SQL dotazu
    query = f"INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES ('{nickname}', '{text}')"

    return query


# Testovací data
author = "JanNovak"
message = "Ahoj, Ondřej Mandík a Alena Reichlová se potkali s Járou Cimrmanem a Petr Novák."
sql_query = create_insert_query(author, message)
print(sql_query)
