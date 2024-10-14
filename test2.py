# Seznam povolených názvů tabulek a sloupců
ALLOWED_TABLES = ["USER"]
ALLOWED_COLUMNS = ["ID", "USERNAME", "PIN", "NAME", "VARIABLE_SYMBOL"]


def is_valid_table(table_name):
    return table_name in ALLOWED_TABLES


def is_valid_column(column_name):
    return column_name in ALLOWED_COLUMNS


def build_sql_select_user_by_username_and_variable_symbol(username, vs):
    # Validace uživatelského jména a proměnného symbolu
    if not isinstance(username, str) or not isinstance(vs, int):
        raise ValueError("Invalid input types.")

    # Validace uživatelského jména
    if not username.isalnum():  # Ověř, že jméno je alfanumerické
        raise ValueError("Invalid username format.")

    return f"SELECT * FROM USER WHERE USERNAME = '{username}' AND VARIABLE_SYMBOL = {vs};"


def build_sql_select_user_by_id(id):
    # Validace ID
    if not isinstance(id, int):
        raise ValueError("Invalid ID type.")
    return f"SELECT * FROM USER WHERE ID = {id};"


def build_sql_select_users_order_by_custom(order_by_section):
    # Zde musíme rozdělit order_by_section na jednotlivé části a validovat každou z nich
    order_by_columns = order_by_section.split(", ")
    for order in order_by_columns:
        # Očekáváme, že order bude mít formát "sloupec ASC|DESC"
        if not any(order.startswith(column) for column in ALLOWED_COLUMNS):
            raise ValueError(f"Invalid order by section: {order}")

    return f"SELECT * FROM USER ORDER BY {order_by_section};"


# Testovací funkce
print(build_sql_select_user_by_id(12))
print(build_sql_select_user_by_username_and_variable_symbol("novak", 1234))
print(build_sql_select_users_order_by_custom("USERNAME DESC, ID"))
