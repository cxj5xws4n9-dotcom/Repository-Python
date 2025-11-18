list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
index = len(list_players) // 2

one_team = list_players[:index]
two_team = list_players[index:]

print(one_team)
print(two_team)