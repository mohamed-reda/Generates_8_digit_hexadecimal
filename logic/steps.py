# from logic.validation import check_all_validations
# from repositories.database_repository import batch_inserts, process_this_selected_number_from_unselected_table, \
#     select_item_randomly, count_of_selected
# 
# 
# def select_from_just_select():
#     pass
# 
# 
# def get_the_final_hex():
#     random_number_from_unselected_list = 0
#     try:
#         b = True
#         while (b):
#             random_number_from_unselected_list = select_item_randomly()
#             batch_inserts(number=10)
#             # random_number_from_unselected_list = 19088743 + (286331153 * 4)
#             if check_all_validations(random_number_from_unselected_list):
#                 print('all validation are checked correctly')
#                 process_this_selected_number_from_unselected_table(random_number_from_unselected_list)
#                 b = False
#             else:
#                 process_this_selected_number_from_unselected_table(number=random_number_from_unselected_list,
#                                                                    just_delete=True)
#                 print('invalid number, so let\'s get another one')
# 
#             count_of_selected()
# 
#     except:
#         print(select_from_just_select())
