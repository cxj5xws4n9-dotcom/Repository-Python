def find_common_participants(group1, group2, sep=','):
    list1 = group1.split(sep)
    list2 = group2.split(sep)
    common = set(list1) & set(list2)
    return sorted(list(common))# TODO Напишите функцию find_common_participants


participants_one_group = "Иванов|Петров|Сидоров"
participants_two_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_one_group, participants_two_group, sep = '|')
print(result)# TODO Проверьте работу функции с разделителем отличным от запятой
