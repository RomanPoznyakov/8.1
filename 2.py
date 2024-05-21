
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Проверяем, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':  
        friends_string = ''
        # Перебираем словарь DATABASE в цикле
        for friend in DATABASE:
            friends_string += friend + ' '  # Добавляем к переменной friends_string имя друга и пробел
        # Возвращаем строку, составленную из 'Твои друзья: ' и friends_string 
        return 'Твои друзья: ' + friends_string  
    # Проверяем, содержит ли переменная query строку 'Где все мои друзья?'
    elif 'Где все мои друзья?' in query:
        return 'Я поняла, это вопрос про города!'
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))
