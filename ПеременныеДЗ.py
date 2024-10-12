count_complete_tasks = 12
count_spent_hours = 1.5
name_of_course = 'Python'
time_for_one_task = count_spent_hours / count_complete_tasks
print('Курс: ' + name_of_course , ' всего задач: ' + str(count_complete_tasks) , ' затрачено часов: ' + str(count_spent_hours), ' среднее время выполенения: ' + str(time_for_one_task) + ' часа.', sep=',')