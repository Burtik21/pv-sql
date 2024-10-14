import sqlite3  # nebo jiný modul pro správu databáze


# Funkce pro aktualizaci emailu uživatele podle ID
def build_sql_update_email_by_id(email, user_id):
    if not isinstance(email, str) or not isinstance(user_id, int):
        raise ValueError("Invalid input types.")

    # Použití parametrizovaného dotazu
    return "UPDATE uzivatel SET email = ? WHERE id = ?", (email, user_id)


# Funkce pro smazání všech záznamů v tabulce
def build_sql_delete_all_by_table(table_name):
    if not isinstance(table_name, str) or not table_name.isidentifier():
        raise ValueError("Invalid table name.")

    # Použití parametrizovaného dotazu
    return f"DELETE FROM {table_name} WHERE 1=1", ()


# Funkce pro aktualizaci uživatelů
def build_sql_update_users(users):
    sql = []
    params = []

    for user in users:
        if not isinstance(user["email"], str) or not isinstance(user["jmeno"], str) or not isinstance(user["id"], int):
            raise ValueError("Invalid user data types.")

        # Použití parametrizovaného dotazu
        sql.append("UPDATE uzivatel SET email = ?, jmeno = ? WHERE id = ?")
        params.append((user["email"], user["jmeno"], user["id"]))

    return sql, params  # Vrátí seznam SQL dotazů a příslušné parametry


# Testovací funkce
print(build_sql_update_email_by_id("ondra@seznam.cz", 23))
print(build_sql_delete_all_by_table("uzivatel"))
print(build_sql_update_users(
    [{"id": 11, "jmeno": "ondra", "email": "ondra@seznam.cz"}, {"id": 12, "jmeno": "petr", "email": "petr@seznam.cz"}]))
