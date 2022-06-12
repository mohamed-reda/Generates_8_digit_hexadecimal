from common import constant


def val1_same_chars(val):
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
    # for ii in range(16):
    #     eq =  (286331153 * ii)
    #     ss = f'{"0x{:08x}".format(eq)}'
    #     print(f"{ii} The hexadecimal of {eq} is _ {ss}")
    b = val % 286331153 != 0
    # if not b:
    #     print('invalid because it has the same same chars')
    return b


def val2_increasing_number(val):
    # for ii in range(9):
    #     eq = 19088743 + (286331153 * ii)
    #     ss = f'{"0x{:08x}".format(eq)}'
    #     print(f"{ii} The hexadecimal of {eq} is _ {ss}")
    b = (val - 19088743) % 286331153 != 0
    # if not b:
    #     print('invalid because it\'s in the invalid list from WIKI')
    return b


def val3_not_on_invalid_list(check_number_list):
    if check_number_list in constant.filtered_invalid_list:
        # print('invalid because it\'s increasing number')
        return False
    return True


def check_all_validations(val):
    if val1_same_chars(val):
        if val2_increasing_number(val):
            if val3_not_on_invalid_list(val):
                return True
    return False
