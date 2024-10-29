def send_email(message, recipient,*, sender = 'g0flou6@gmail.com'):
    if '@' not in recipient or '@' not in sender or not recipient.endswith('.com') or not sender.endswith('.com'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'g0flou6@gmail.com':
        print(f'Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Проверка связи', 'dragonslayer228@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'g0flou6@gmail.com', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'g0flou6@gmail.com', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'g0flou6@gmail.com')