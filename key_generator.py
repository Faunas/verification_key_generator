import socket
import uuid
from database import *
import getpass

name_pc = getpass.getuser()
uuid = uuid.getnode()
user_ip = socket.gethostbyname(socket.gethostname())

print(
    "Для получения самого ключа - обратитесь к администратору системы с просьбой выдать ключ доступа.\nПосле получения ключа введите его в программу.'\n"
    "Если ключ всё ещё не подходит, убедитесь, что вы написали его верно и без лишних пробелов.\n"
    "Если вы сделали всё правильно, то уведомление о неверном ключе доступа не появится.\nПриятного использования! :)\n\n\n")


def all_info_about_user():
    print(f"Название пользователя: {name_pc}\nУникальный идентификатор: {uuid}\nАйпи адрес: {user_ip}\n")


all_info_about_user()
if is_new_user(uuid):
    print("У вас нет прав использовать эту программу.")
    insert_all_date_about_user(name_pc=name_pc, uuid=uuid, ip=user_ip)
    quit()

user_key = str(input("Введите ключ доступа: "))
with open("key.txt", "w") as f:
    f.write(user_key)  # запись ключа в файл

with open("key.txt", "r") as f:
    user_key = str(f.readline().strip())  # Чтение ключа из файла
    # print(user_key)

if user_key != key_from_db(uuid):
    key = key_from_db(uuid)
    print("Ошибка: неверный ключ доступа")
    exit()

print("Добро пожаловать! Вы успешно подтвердили свою личность!")
