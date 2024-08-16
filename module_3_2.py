def send_email(massage, recipient, *, sender="university.help@gmail.com"):
    a = "@"
    while 1 > 0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if a not in recipient and sender:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                break
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            break
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            break
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            break
        elif sender != "university.help@gmail.com":
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
            break


send_email(input("Введите сообщение: "), input("Введите адрес электронной почты: "))
