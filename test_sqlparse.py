import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML

sql = """
select 
t.kod, 
t.nazev,
d.datum,
p.nazev,
h.nazev
from tabulka t 
inner join datumy d on d.datum_ck=t.datum_ck
left join produkty p on p.produkt_ck=t.produkt_ck
left join historie h on h.datum_ck between t.datum_ck and t.datum_do_ck
where t.obdobi = 2025 
"""

parsed = sqlparse.parse(sql)[0]  # první statement
# for token in parsed.tokens:
#     print(f"{str(token.ttype):<40} {str(token):<20} {str(type(token))}")

# for token in parsed.tokens:
#     if token.ttype is Keyword and "JOIN" in token.value.upper():
#         print("JOIN část:", token)

i = 0
tmp = parsed.tokens
flg = False
pom = []
res = []
while i < len(tmp):
    # print(f"{i:<20} {str(tmp[i]):<20}")
    if "join" in tmp[i].value.lower() \
        and not ("where" in tmp[i].value.upper() \
        or "order" in tmp[i].value.upper() \
        or "group" in tmp[i].value.upper()):
        if len(pom) > 0:
            res.append(pom)
        flg = True
        pom = []
    if "where" in tmp[i].value.upper() \
        or "order" in tmp[i].value.upper() \
        or "group" in tmp[i].value.upper():
        flg = False
    if flg:
        pom.append(str(tmp[i]))
        print(pom)
    i += 1
print(res)
