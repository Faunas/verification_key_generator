from MySQLdb import connect, cursors, Error

MYSQLCONF = {
    'host': 'localhost',  # хост базы данных
    'user': 'TestUser',  # имя пользователя базы данных
    'password': 'TestUser',  # пароль пользователя базы данных
    'db': 'test',  # имя базы данных
    'charset': 'utf8',  # используемая кодировка базы данных
    'autocommit': True,  # автоматический cursor.commit()
    # извлекаемые строки из БД принимают вид словаря
    'cursorclass': cursors.DictCursor
}


def test_connection():
    db = connect(**MYSQLCONF)
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM `keys_users`')
    result = cursor.fetchall()
    db.close()
    return result


# Проверка, если пользователя нет в базе данных
def is_new_user(uuid):
    db = connect(**MYSQLCONF)
    cursor = db.cursor()
    cursor.execute(f'SELECT `user_key` FROM `keys_users` WHERE `uuid` = {uuid}')
    result = cursor.fetchall()
    if len(result) == 0:
        print("[LOGS] Пользователя нет в базе данных.")
        return True
    else:
        print("[LOGS] Пользователь есть в базе данных.")
        return False


def insert_all_date_about_user(name_pc, uuid, ip):
    db = connect(**MYSQLCONF)
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO `keys_users` (`id`, `name`, `uuid`, `ip`) VALUES (NULL, '{name_pc}', '{uuid}', '{ip}')")

    db.close()


def key_from_db(uuid):
    db = connect(**MYSQLCONF)
    cursor = db.cursor()
    cursor.execute(f'SELECT `user_key` FROM `keys_users` WHERE `uuid` = {uuid}')
    result = cursor.fetchall()
    db.close()
    return str(result[0]['user_key'])
