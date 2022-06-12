import sqlite3

from logic.format_to_hex import get_hex


def batch_inserts(number: int = 10):
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    try:

        #  cur.execute('''CREATE TABLE IF NOT EXISTS SELECTED(
        #  ID INTEGER PRIMARY KEY AUTOINCREMENT,
        # SELECTED_LIST CHAR(255) )''')
        cur.execute('''CREATE TABLE UNSELECTED(
        ID INTEGER PRIMARY KEY)''')
        cur.execute('''CREATE TABLE SELECTED(
        ID INTEGER PRIMARY KEY)''')
        l = []
        for i in range(number + 1):
            l.append((i,))
        # print('the table is created Now')
        con.executemany("insert into UNSELECTED(ID) values (?)", l)
        con.commit()

    except sqlite3.OperationalError:
        pass
        # print('you already created the table before')
    except sqlite3.DatabaseError:
        print('DatabaseError')
    except sqlite3.Error:
        print('DataError')

    cur.close()


# 
# def drop_table_unselected():
#     con = sqlite3.connect("lists.db")
#     cur = con.cursor()
#     cur.execute(''' DROP table UNSELECTED;''')
#     con.commit()
#     cur.close()

# def print_selected():
#     con = sqlite3.connect("lists.db")
#     cur = con.cursor()
#     c = cur.execute('''SELECT Count()  FROM UNSELECTED;''')
#     l = c.fetchall()
#     print(l[0])
#     c = cur.execute('''SELECT Count()  FROM SELECTED;''')
#     l = c.fetchall()
#     print(l[0])
#     con.commit()
#     cur.close()


def count_of_selected():
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    c = cur.execute('''SELECT Count()  FROM SELECTED;''')
    # print(f'the size of the selected is {c.fetchall()[0][0]}')
    con.commit()
    cur.close()


def process_this_selected_number_from_unselected_table(number: int, just_delete: bool = False):
    # print('--------------------------------------------')
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    cur.execute(f'''DELETE FROM UNSELECTED WHERE ID ={number};''')
    if not just_delete:
        cur.execute(f'''INSERT  INTO SELECTED  (ID) values({number});''')
        # print('inserted into selected correctly')

    # print(f'the random number is moved correctly')
    # print('--------------------------------------------')
    con.commit()
    cur.close()


def just_select_and_print():
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    c = cur.execute('''SELECT * FROM UNSELECTED ORDER BY RANDOM() LIMIT 1;''')
    # c = cur.execute('''SELECT Count()  FROM UNSELECTED;''')
    # c = cur.execute('''SELECT *  FROM UNSELECTED;''')
    try:
        l = c.fetchall()
        if len(l) != 0:
            print(f'you chose {l[0][0]} as a random number from the selected list\nits hex is {get_hex(l[0][0])}')
            con.commit()
        else:
            # c = cur.execute('''SELECT * FROM SELECTED ORDER BY RANDOM() LIMIT 1;''')
            # l = c.fetchall()
            # drop_table_unselected()
            cur.execute('''ALTER TABLE UNSELECTED RENAME TO SELECTED1;''')
            con.commit()
            cur.execute('''ALTER TABLE SELECTED RENAME TO UNSELECTED;''')
            con.commit()
            cur.execute('''ALTER TABLE SELECTED1 RENAME TO SELECTED;''')
            con.commit()
            c = cur.execute('''SELECT * FROM UNSELECTED ORDER BY RANDOM() LIMIT 1;''')
            con.commit()
            cur.execute('''CREATE TABLE IF NOT EXIST SELECTED(
                    ID INTEGER PRIMARY KEY)''')

    except IndexError:
        print('this is an empty list')

    cur.close()


def select_item_randomly():
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    c = cur.execute('''SELECT * FROM UNSELECTED ORDER BY RANDOM() LIMIT 1;''')
    # c = cur.execute('''SELECT Count()  FROM UNSELECTED;''')
    # c = cur.execute('''SELECT *  FROM UNSELECTED;''')
    try:
        l = c.fetchall()
        if len(l) == 0:
            # drop_table_unselected()
            cur.execute('''ALTER TABLE UNSELECTED RENAME TO SELECTED1;''')
            con.commit()
            cur.execute('''ALTER TABLE SELECTED RENAME TO UNSELECTED;''')
            con.commit()
            cur.execute('''ALTER TABLE SELECTED1 RENAME TO SELECTED;''')
            con.commit()
            c = cur.execute('''SELECT * FROM UNSELECTED ORDER BY RANDOM() LIMIT 1;''')
            con.commit()
            l = c.fetchall()

            # cur.execute('''CREATE TABLE IF NOT EXIST SELECTED(
            #         ID INTEGER PRIMARY KEY)''')

    except IndexError:
        print('this is an empty list')

    cur.close()
    return l[0][0]
