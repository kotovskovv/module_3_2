def send_email(message, recipient, sender='university.help@gmail.com'):
    if ('@' and ('.com' or '.ru' or '.net') not in (recipient or sender)) or (
            '@' or ('.com' or 'ru' or '.net')) not in (recipient or sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != "university.help@gmail.com":
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'kotovskovv@bk.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@yandex.ru')
send_email('Это сообщение для проверки связи', 'urban@gmail.com')
send_email('Напоминаю самому себе о лекции', 'university.help@gmail.com', sender='vasyok1337@yandex.ru')
send_email('Вы видите это сообщение как лучший студент курса', 'university.help@gmail.com',
           sender='university.help@gmail.com')
