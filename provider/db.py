class Database:
    users = []

    def get(user=None):
        if user:
            return users.get(user)
        else:
            return users

    def add(username, password):
        if username in users:
            return False
        else:
            users[username] = password
