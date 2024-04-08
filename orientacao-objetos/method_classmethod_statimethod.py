class Connection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x, y):
        return x + y


c1 = Connection()
# print(c1.user)
c1.set_user('root')
c1.set_password('root')
print(c1.user)
print(c1.password)

c2 = Connection.create_with_auth('admin', 'admin')
print(Connection.soma(1, 1))
print(c2.user)
print(c2.password)
