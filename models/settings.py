from models.DB import *


def insert_user(login: str, full_name: str, password: str, author: int) -> int:
    result = DB.insert_users(login, full_name, password)
    if result != 0:
        return 1
    if author == 1:
        result2 = DB.insert_authors(DB.get_user(login))
        print(result2)
        if result2 != 0:
            return 1
        return 0
    

def auth_user(login: str, password: str) -> int:
    result = DB.auth_user(login)
    if password == result[0]:
        return 0
    return 1


def get_users_data(login: str) -> list:
    result1 = DB.get_users_data(login)
    result2 = DB.get_users_root(login)
    result1 += result2
    return result1

def insert_article(title: str, text: str, author_id: int):
    result = DB.insert_articles(title, text, author_id)
    return result


def get_all_artcs() -> list:
    result = DB.get_all_artcs()
    return result


def insert_rate(rate: int, text: str, user_id: int, artcs_id: int):
    result = DB.insert_ratings(user_id=user_id, rate=rate, article_id=artcs_id, text=text)
    return result


def get_all_comments() -> list:
    result = DB.get_all_ratings()
    return result
