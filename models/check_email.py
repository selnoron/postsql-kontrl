class Check:
    """Check email"""

    @staticmethod
    def check_email(em) -> bool:
        _pattern_email = [
            'gmail.com', 'mail.ru', 'yandex.ru',
            'kahoo.com', 'yahoo.com', 'od.ru',
            'github.com', 'hotmail.com', 'tempmail.ru'
        ]
        email_elements: list[str] = em.split("@")
        if "" in email_elements:
            return False

        if len(email_elements) != 2:
            return False
        
        if email_elements[0] != email_elements[0].lower():
            return False

        if not email_elements[1] in _pattern_email:
            return False

        return True