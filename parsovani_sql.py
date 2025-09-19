"""
Tento skript analyzuje SQL dotaz a extrahuje 
tabulky a sloupce pomocí knihovny sql_metadata.
"""

from sql_metadata import Parser

def main():
    """
    Hlavní funkce pro analýzu SQL dotazu.
    """
    # query = """
    # SELECT e.employee_id,
    #        e.first_name,
    #        d.department_name
    # FROM employees e
    # JOIN departments d ON e.department_id = d.department_id
    # WHERE e.salary > 5000
    # """
    query = """
    select
    a.pk_id,
    b.flg,
    a.dim1,
    sum(a.meas1) as suma
    from TabA a
    inner join TabB b on a.flg_id=b.flg_id
    where a.dim1 = 'a'
    """

    parser = Parser(query)

    print("Tabulky:", parser.tables)
    print("Sloupce:", parser.columns)
    print("Sloupce:", parser.columns_dict)

if __name__ == "__main__":
    main()
