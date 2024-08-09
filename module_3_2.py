def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient and sender:
       return print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient, '.')

    if not (sender.endswith('.ru') or sender.endswith('.com') or sender.endswith('.net')):
        return print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient, '.')

    if not (recipient.endswith('.ru') or recipient.endswith('.com') or recipient.endswith('.net')):
        return print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient, '.')

    if sender == recipient:
        return print("Нельзя отправить письмо самому себе!")

    if sender == 'university.help@gmail.com':
        return print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)

    else:
        return print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient, '.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')