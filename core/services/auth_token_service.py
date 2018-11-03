class AuthTokenService:
    def make_auth_token(self, user):
        return str(user.id)

    def extract_user_id(self, token):
        return int(token)
