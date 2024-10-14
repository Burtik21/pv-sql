import sqlite3  # nebo jiný modul pro správu databáze


def build_sql_update_user_jmeno_by_id(name, id):
    if not isinstance(name, str) or not isinstance(id, int):
        raise ValueError("Invalid input types.")

    # Použití parametrizovaného dotazu
    return "UPDATE uzivatel SET jmeno = ? WHERE id = ?", (name, id)


def build_sql_delete_by_table_and_id(table_name, id):
    if not isinstance(id, int) or not isinstance(table_name, str) or not table_name.isidentifier():
        raise ValueError("Invalid table name or ID type.")

    # Použití parametrizovaného dotazu
    return f"DELETE FROM {table_name} WHERE id = ?", (id,)


def build_sql_insert_users(users):
    sql = []
    params = []
    for user in users:
        if not isinstance(user["email"], str) or not isinstance(user["jmeno"], str):
            raise ValueError("Invalid user data types.")

        # Použití parametrizovaného dotazu
        sql.append("INSERT INTO uzivatel (email, jmeno) VALUES (?, ?)")
        params.append((user["email"], user["jmeno"]))

    return sql, params  # Vrátí seznam SQL dotazů a příslušné parametry


# Testovací funkce
print(build_sql_update_user_jmeno_by_id("martin", 38))
print(build_sql_delete_by_table_and_id("uzivatel", 42))
print(build_sql_insert_users(
    [{"jmeno": "ondra", "email": "ondra@seznam.cz"}, {"jmeno": "petr", "email": "petr@seznam.cz"}]))
