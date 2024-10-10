team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


percent_first_string = "В команде Мастера кода участников: %s!"
percent_second_string = "Итого сегодня в командах участников: %s и %s!"

print(percent_first_string % team1_num)
print(percent_second_string % (team1_num, team2_num))

format_first_string = "Команда Волшебники данных решила задач: {}!"
format_second_string = "Волшебники данных решили задачи за {} с !"

print()
print(format_first_string.format(score_2))
print(format_second_string.format(team1_time))

f_first_string = f"Команды решили {score_1} и {score_2} задач."
f_second_string = f"Результат битвы: {challenge_result}!"
f_third_string = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

print()
print(f_first_string)
print(f_second_string)
print(f_third_string)
