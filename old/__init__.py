import sqlite3


def create_database():
    con = sqlite3.connect("lists.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS SELECTED(
    ID INTEGER PRIMARY KEY
    )''')

    for i in range(1, 100000000):
        # s = f'{"0x{:08x}".format(i)}'
        # # print(s)

        cur.execute(f'''insert into SELECTED
                    (ID) values
                    ({i});''')
    con.commit()

    # i = 0
    # for row in c:
    #     # i = row[0]
    #     # print(i)
    #     print(row)
    # print(i)

    #  cur.execute('''CREATE TABLE UNSELECTED(
    #  ID INTEGER PRIMARY KEY AUTOINCREMENT,
    # UNSELECTED_LIST INT)''')

    #  cur.execute(''' SELECT UNSELECTED_LIST FROM UNSELECTED  ''')
    # cur.execute()
    cur.close()
