class UserService:
    def __init__(self, user_dao):
        self.__user_dao = user_dao

    def add(self, user):
        existing_user = self.__user_dao.find_by_username(user.username)
        if existing_user:
            raise Exception('User {} already exists'.format(user.username))

        self.__user_dao.add(user)

    def update(self, user):
        existing_user = self.__user_dao.find(user.id)
        if not existing_user:
            raise Exception('User not found')

        user_with_same_username = self.__user_dao.find_by_username(user.username)
        if not user_with_same_username or user_with_same_username.id != user.id:
            raise Exception('Cannot change username')

        self.__user_dao.update(user)

    def remove(self, user):
        self.__user_dao.remove(user.id)