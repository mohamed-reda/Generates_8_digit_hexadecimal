from common import constant

from datetime import datetime

from logic.format_to_hex import get_hex
from logic.validation import check_all_validations
from repositories.database_repository import batch_inserts, process_this_selected_number_from_unselected_table, \
    select_item_randomly, count_of_selected


def get_the_final_hex():

    batch_inserts()
    b = True
    while b:
        random_number_from_unselected_list = select_item_randomly()
        batch_inserts(number=constant.MaxNumber)
        if check_all_validations(random_number_from_unselected_list):
            # print('all validation are checked correctly')
            # move the number to the selected table and remove it from unselected
            process_this_selected_number_from_unselected_table(random_number_from_unselected_list)
            b = False
            print(f'{get_hex(random_number_from_unselected_list)}')
        else:
            # delete this invalid number then the while loop will loop again
            process_this_selected_number_from_unselected_table(number=random_number_from_unselected_list,
                                                               just_delete=True)
            # print('invalid number, so let\'s get another one')
        count_of_selected()


if __name__ == '__main__':
    # started = datetime.now().strftime("%H:%M:%S")
    get_the_final_hex()

    # print(started)
    # print(datetime.now().strftime("%H:%M:%S"))
