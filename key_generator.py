import socket
import uuid
from database import *
import getpass

name_pc = getpass.getuser()
uuid = uuid.getnode()
user_ip = socket.gethostbyname(socket.gethostname())

question = int(input("Вывести инструкцию по установке ключа (1/0)?: "))
if question == 1:
    print(
        "Для получения самого ключа - обратитесь к администратору системы с просьбой выдать ключ доступа.\nПосле получения ключа введите его в файл 'key.txt'\n"
        "Если ключ всё ещё не подходит, убедитесь, что в файле нет лишних пробелов в начале или конце.\n"
        "Если вы сделали всё правильно, то уведомление о неверном ключе доступа не появится.\nПриятного использования! :)")


def all_info_about_user():
    print("Название пользователя:", name_pc)
    print("Уникальный идентификатор:", uuid)
    print("Айпи адрес:", user_ip)


all_info_about_user()
if is_new_user(uuid):
    print("У вас нет прав использовать эту программу.")
    insert_all_date_about_user(name_pc=name_pc, uuid=uuid, ip=user_ip)
    quit()

with open("key.txt", "r") as f:
    user_key = str(f.readline().strip())
    # print(user_key)

if user_key != key_from_db(uuid):
    key = key_from_db(uuid)
    # print(key)
    print("Ошибка: неверный ключ доступа")
    exit()


print("Добро пожаловать!")
