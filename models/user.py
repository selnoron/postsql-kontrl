from models.check_email import *


class User:
    """User registration/authentication"""

    def __init__(
        self,
        login: str,
        password: str,
        email: str,
        name: str,
        surname: str,
        age: str
    ) -> None:
        self.login = login
        self.password = password
        self.email = email
        self.name = name
        self.surname = surname
        self.age = age
        self.admin = False
    
    @staticmethod
    def administration(
        user: "User"
    ) -> str:
        user.admin = True
        return True

    @staticmethod
    def check_login_unique(
        login: str,
        users_data: list['User']
    ) -> str:
        for user in users_data:
            if user.login == login:
                return "\nlogin is not unique"
        return ''
            
    @staticmethod
    def check_normal_age(
        age: int
    ) -> str:
        if age < 0 and age > 121:
            return "\nAge cant be under than 0 and upper than 120"
        return ''
    
    @staticmethod
    def check_all(
        login: str,
        user_data: list['User'],
        age: int,
        email: str
    ) -> str:
        errors: str = ''
        errors += User.check_login_unique(login, user_data)
        errors += User.check_normal_age(age)
        print(age < 0, age > 121)
        if not Check.check_email(email):
            errors += "\nEmail is not correct"
        return errors
