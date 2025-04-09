from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "admin"
        self.password = "123456"  # pode usar dotenv ou base de dados depois
