import re

def remove_html_tags(text):
    return re.sub(r'<.*?>', '', text)

def escape_special_chars(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;"))

def sanitize_input(text):
    text = remove_html_tags(text)
    text = escape_special_chars(text)
    return text

def build_html_news_item(label, text):
    label_clean = sanitize_input(label)
    text_clean = sanitize_input(text)
    return f'<div class="news_item"><h2>{label_clean}</h2><p>{text_clean}</p></div>'

def build_html_head_by_author(author):
    author_clean = sanitize_input(author)
    headersHtml = ""
    headersHtml += '<meta name="copyright" content="All rights reserved to author" />\n'
    headersHtml += f'<meta name="author" content="{author_clean}" />\n'
    return headersHtml

def build_xml_from_users(users):
    xml = "<users>\n"
    for user in users:
        username_clean = sanitize_input(user["username"])
        phone_clean = sanitize_input(user["phone"])
        xml += f" <user>\n"
        xml += f"  <username>{username_clean}</username>\n"
        xml += f"  <phone>{phone_clean}</phone>\n"
        xml += f" </user>\n"
    xml += "</users>\n"
    return xml

print(build_html_news_item("Výprodej zboží", "Od následujícího měsíce budou slevy až 50%"))
print(build_html_head_by_author("Petr Novák"))
print(build_xml_from_users([
    {"username": "novak34", "phone": "605123654"},
    {"username": "svoboda2", "phone": "774123654"}
]))

print(build_html_news_item("Výprodej zboží", "Od následujícího měsíce budou slevy až 50%</p></div><script>alert('Hacked!');</script><p><div>"))
print(build_html_head_by_author('Petr Novák"/><script type="text/javascript" src="http://hackeruv-server.net/xss.js" /><meta name="description" content="Hacked site!'))
print(build_xml_from_users([
    {"username": "novak34", "phone": "605123654</phone>\n </user> \n<user>\n  <username>hacker</username>\n  <phone>123123123"},
    {"username": "svoboda2", "phone": "774123654"}
]))
