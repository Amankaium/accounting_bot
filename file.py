from time import sleep
from json import loads
from requests import get
from mytoken import token

f = open("answered.txt", mode="r+", encoding="utf-8")
answered_lst = f.read().split()
# print(answered_lst)

while True:
    sleep(1)
    r = get(f"https://api.telegram.org/bot{token}/getUpdates")
    d = loads(r.text)

    for update in d["result"]:
        message_id = update["message"]["message_id"]
        # print(message_id)
        # print(answered_lst)
        if str(message_id) not in answered_lst:
            # print("нет с списке")
            chat = update["message"]["chat"]["id"]
            message = "Теперь на это сообщение ответили"
            get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text={message}")
            f.write(str(message_id) + "\n")
            answered_lst.append(str(message_id))

f.close()
