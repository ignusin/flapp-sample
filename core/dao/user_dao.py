from flapp.persistence.dao import AbstractDAO
from ..objects import User

class UserDAO(AbstractDAO):
    class UserMapper:
        def map_to_object(self, record):
            return User(**record)

        def map_to_db_values(self, obj):
            return (obj.id, obj.username, obj.password)


    __table_name__ = 'users'
    __fields__ = ('id', 'username', 'password')
    __mapper__ = UserMapper()

    def __init__(self, cursor_factory):
        super().__init__(cursor_factory)

    def find_by_credentials(self, username, password):
        with self.with_cursor() as cur:
            cur.execute('SELECT "id", "username", "password" FROM "users" WHERE "username"=%s AND "password"=%s', (username, password))
            return self.map(cur.fetchone())

        return User(id=1)
