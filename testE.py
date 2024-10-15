import re

# Funkce pro odstranění HTML/XML tagů
def remove_html_tags(text):
    return re.sub(r'<.*?>', '', text)

# Funkce pro nahrazení speciálních znaků HTML/XML escapováním
def escape_special_chars(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;"))

# Kombinovaná funkce pro odstranění tagů a escapování speciálních znaků
def sanitize_input(text):
    text = remove_html_tags(text)  # Odstraní HTML/XML tagy
    text = escape_special_chars(text)  # Escapuje zbylé speciální znaky
    return text

# Opravené funkce pro generování HTML a XML s ošetřením
def build_html_contact_item(name, phone):
    name_clean = sanitize_input(name)
    phone_clean = sanitize_input(phone)
    return f'<div class="contact_item"><h2>{name_clean}</h2><p>Phone: {phone_clean}</p></div>'

def build_html_img(path, width, height, description=""):
    path_clean = sanitize_input(path)
    description_clean = sanitize_input(description)
    return f'<img src="{path_clean}" alt="{description_clean}" width="{width}" height="{height}">'

def build_xml_from_money_transactions(money_transactions):
    xml = "<money_transactions>\n"
    for transaction in money_transactions:
        account_number_clean = sanitize_input(transaction["account_number"])
        amount_clean = sanitize_input(str(transaction["amount"]))
        message_clean = sanitize_input(transaction["message"])
        xml += f" <transaction>\n"
        xml += f"  <account_number>{account_number_clean}</account_number>\n"
        xml += f"  <amount>{amount_clean}</amount>\n"
        xml += f"  <message>{message_clean}</message>\n"
        xml += " </transaction>\n"
    xml += "</money_transactions>\n"
    return xml

# Testovací funkce
# Bezpečné vstupy
print(build_html_contact_item("Ing. Jan Novák", "+420 606321423"))
print(build_html_img("/img/obrazek.jpg", 80, 40, "Logo firmy"))
print(build_xml_from_money_transactions([
    {"account_number": "0500021502/0800", "amount": 1300, "message": "Platba za obědy Jan Novák"},
    {"account_number": "1500023322/0600", "amount": 1450, "message": "Obědy Petr Novák"}
]))

# Nebezpečné vstupy (budou očištěny)
print(build_html_contact_item("Ing. Jan Novák", "+420 606321423</p></div><script>alert('Hacked!');</script><p><div>"))
print(build_html_img("/img/obrazek.jpg", 80, 40, "\"/><img src=\"\" width=\"100\" height=\"200\" alt=\"Hacked logo"))
print(build_xml_from_money_transactions([
    {"account_number": "0500021502/0800", "amount": 1300, "message": "Platba za obědy Jan Novák"},
    {"account_number": "1500023322/0600", "amount": 1450, "message": "Obědy Petr Novák</message>\n </transaction>\n <transaction>\n  <account_number>0700098720/0100</account_number>\n  <amount>1000000</amount>\n"}
]))
