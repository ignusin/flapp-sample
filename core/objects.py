from flapp.persistence.persistent_object import make_persistent_object

User = make_persistent_object('User', ('id', 'username', 'password'))
