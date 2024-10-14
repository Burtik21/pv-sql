# Seznam povolených názvů tabulek a sloupců
ALLOWED_TABLES = ["USER"]
ALLOWED_COLUMNS = ["ID", "USERNAME", "PIN", "NAME", "VARIABLE_SYMBOL"]


def is_valid_table(table_name):
    return table_name in ALLOWED_TABLES


def is_valid_column(column_name):
    return column_name in ALLOWED_COLUMNS


# Library of functions
def build_sql_select_all_from_table(table_name):
    if not is_valid_table(table_name):
        raise ValueError("Invalid table name")
    return f"SELECT * FROM {table_name}"


def build_sql_select_custom_from_users(columns):
    
    for column in columns:
        if not is_valid_column(column):
            raise ValueError(f"Invalid column name: {column}")

    sql = "SELECT "
    sql += ", ".join(columns)
    sql += " FROM USER"
    return sql


def build_sql_select_users_order_by_custom(order_by_section):

    order_by_columns = order_by_section.split(", ")
    for order in order_by_columns:
        # Očekáváme, že order bude mít formát "sloupec ASC|DESC"
        if not any(order.startswith(column) for column in ALLOWED_COLUMNS):
            raise ValueError(f"Invalid order by section: {order}")

    return f"SELECT * FROM USER ORDER BY {order_by_section}"


# Testovací funkce
print(build_sql_select_all_from_table("USER"))
print(build_sql_select_custom_from_users(["NAME", "USERNAME"]))
print(build_sql_select_users_order_by_custom("USERNAME DESC, ID"))
