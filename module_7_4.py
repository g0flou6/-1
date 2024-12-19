team1_num = 10
team1_name = 'Мастера кода'
team2_num = 11
team2_name = 'Волшебники данных'
print('В команде %(name)s участников: %(num)s!' %{'name': team1_name, 'num': team1_num})
print('Итого сегодня в командах участников: %(num1)s и %(num2)s.' %{'num1': team1_num, 'num2': team2_num})
score_1 = 40
score_2 = 41
print('Команда {name} решила задач: {score}!'.format(name= team2_name, score= score_2))
time_1 = 1505.5
time_2 = 1801.2
print('Команда {name} решила задачи за {time} секунд.'.format(name= team2_name, time= time_2))
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and time_1 < time_2:
    result = f'Победа команды {team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and time_1 > time_2:
    result = f'Победа команды {team2_name}!'
else:
    result = 'Ничья!'
challenge_result = result
print(challenge_result)
tasks_total = score_1 + score_2
avg_time = (time_1 + time_2) // tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {int(avg_time)} секунд на задачу!')

