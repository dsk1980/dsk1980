team_1 = '"Мастера кода"'
team_2 = '"Волшебники данных"'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
total_time = team1_time + team2_time
time_avg = tasks_total / total_time

# Использование %:
print('В команде %s участников: %s!' % (team_1, team1_num))
print('В команде %s участников: %s!' % (team_2, team2_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print()


# Использование format():
print('Команда {} решила задач: {}!'.format(team_1, score_1))
print('Команда {} решила задач: {}!'.format(team_2, score_2))
print('{} решили задачи за {} сек.!'.format(team_1, team1_time))
print('{} решили задачи за {} сек.!'.format(team_2, team2_time))
print()

# Использование f-строк:
print(f'"Команды решили {score_1} и {score_2} задачи.”')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды ' + team_1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды ' + team_2
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')
