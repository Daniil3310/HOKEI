# Список всех удалений в формате: (номер команды, продолжительность удаления)
penalties = [
    (1, 2), (2, 5), (1, 10), (2, 2), (1, 5),
    (1, 10), (2, 5), (2, 2), (1, 2), (2, 10),
    (1, 5), (2, 10), (1, 2), (1, 5), (2, 10),
    (2, 5), (1, 2), (2, 10), (1, 5), (2, 2),
    (1, 10), (1, 2), (2, 5), (1, 5)
]

# Функция для вычисления общих удалений и времени для каждой команды
def calculate_penalties(penalties):
    team_stats = {1: {'count': 0, 'time': 0}, 2: {'count': 0, 'time': 0}}
    
    # Проходим по всем удалениями
    for team, time in penalties:
        team_stats[team]['count'] += 1
        team_stats[team]['time'] += time
    
    return team_stats

# Получаем статистику
stats = calculate_penalties(penalties)

# Выводим результаты
for team, stat in stats.items():
    print(f"Команда {team}: Удалений: {stat['count']}, Время удалений: {stat['time']} минут")
