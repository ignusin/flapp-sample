1. Application context: core/context.py
2. DI usage: api/auth.py : @uses decorator for "authorize" and "register" flask handlers
3. Persistent objects: core/objects.py
4. Validator declaration: core/validators.py
5. Validator usage: api/auth.py : @validated decorator for "register" flask handler
6. DAO: core/dao/user_dao.py
7. Service: core/services/user_service.py
