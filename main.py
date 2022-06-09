import sqlite3
import constant

from datetime import datetime

x = 4, 294, 967, 295
until_valid = 4294967294


def get_hex():
    # print(len('DEADBEEF'))
    # bytes.fromhex('68656c6c6f').decode('utf-8')
    # print(int('68656c6c6f', 8))
    hex_val = '0x10000000'

    # The hexadecimal form of 4294967295 is _ 0xffffffff, 10

    print(x)
    for i in range(x - 10, x + 10):
        s = f'{"0x{:08x}".format(i)}'
        print(f"The hexadecimal form of {i} is _ {s}, {len(s)}")

    # s = f'{"0x{:08x}".format(1044942)}'
    # print(f"The hexadecimal form of {1044942} is _ {s}, {len(s)}")


def filtered():
    l = []
    for i in range(len(constant.invalidlist)):
        if constant.invalidlist[i] < x:
            l.append(constant.invalidlist[i])
    print(l)


def clear():
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    cur.execute(''' DROP table SELECTED;''')
    con.commit()
    cur.close()


def save_string():
    l = range(constant.MaxNumber)
    print(len(l))
    s = str(l)
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS SELECTED(
        LIST CHAR
        )''')
    sql = f'''insert into SELECTED
                        (ID) values
                        ({s});'''
    cur.execute(sql)
    con.commit()
    cur.close()


def select_table():
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    c = cur.execute('''SELECT * FROM SELECTED;''')
    # c = cur.execute('''SELECT Count()  FROM SELECTED;''')
    # c = cur.execute('''SELECT *  FROM SELECTED;''')

    l = c.fetchall()
    # for row in c:
    #     i = row[0]
    #     print(i)
    #     l.append(c)
    print(len(l))
    con.commit()
    cur.close()


def val1_same_chars():
    # The hexadecimal of 0 is _ 0x00000000
    # The hexadecimal of 1 is _ 0x00000001
    # The hexadecimal of 2 is _ 0x00000002
    # The hexadecimal of 3 is _ 0x00000003
    # The hexadecimal of 4 is _ 0x00000004
    # The hexadecimal of 5 is _ 0x00000005
    # The hexadecimal of 6 is _ 0x00000006
    # The hexadecimal of 7 is _ 0x00000007
    # The hexadecimal of 8 is _ 0x00000008
    # The hexadecimal of 9 is _ 0x00000009
    # The hexadecimal of 10 is _ 0x0000000a
    # The hexadecimal of 11 is _ 0x0000000b
    # The hexadecimal of 12 is _ 0x0000000c
    # The hexadecimal of 13 is _ 0x0000000d
    # The hexadecimal of 14 is _ 0x0000000e
    # The hexadecimal of 15 is _ 0x0000000f
    for ii in range(16):
        eq =  (286331153 * ii)
        ss = f'{"0x{:08x}".format(eq)}'
        print(f"{ii} The hexadecimal of {eq} is _ {ss}")


def val2_increasing_number():
    for ii in range(9):
        eq = 19088743 + (286331153 * ii)
        ss = f'{"0x{:08x}".format(eq)}'
        print(f"{ii} The hexadecimal of {eq} is _ {ss}")


def val3_not_on_invalid_list():
    print('')


def batch_inserts():
    con = sqlite3.connect("lists.db")
    cur = con.cursor()
    # cur.execute(''' DROP table SELECTED;''')

    #  cur.execute('''CREATE TABLE IF NOT EXISTS SELECTED(
    #  ID INTEGER PRIMARY KEY AUTOINCREMENT,
    # SELECTED_LIST CHAR(255) )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS SELECTED(
    ID INTEGER PRIMARY KEY)''')
    l = []
    for i in range(1, 100000000):
        l.append((i,))
    print('list is created')
    con.executemany("insert into SELECTED(ID) values (?)", l)
    #  cur.execute('''CREATE TABLE UNSELECTED(
    #  ID INTEGER PRIMARY KEY AUTOINCREMENT,
    # UNSELECTED_LIST INT)''')

    con.commit()
    cur.close()


if __name__ == '__main__':
    # get_hex()
    started = datetime.now().strftime("%H:%M:%S")
    # select_table()
    # batch_inserts()
    # clear()
    # save_string()
    # val2_increasing_number()
    # i = 18369614221190020847
    # s = f'{"0x{:08x}".format(i)}'
    # print(f"The hexadecimal form of {i} is _ {s}, {len(s)}")
    # val2_increasing_number()
    val2_increasing_number()
    print(started)
    print(datetime.now().strftime("%H:%M:%S"))
    print('done')
# (1, '0x00000000')

# (10, '0x00000009')
