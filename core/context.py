from contextlib import contextmanager

from config import config

from flapp import di
from flapp.persistence.connection import (
    create_connection_factory, create_connection_pool, create_cursor_factory)

from .dao import UserDAO
from .services import UserService

db_connection_pool = create_connection_pool(**config['db'])
db_connection_factory = create_connection_factory(db_connection_pool)
db_cursor_factory = create_cursor_factory(db_connection_factory)

user_dao = di.instance('user_dao', UserDAO(db_cursor_factory))
user_service = di.instance('user_service', UserService(user_dao))
