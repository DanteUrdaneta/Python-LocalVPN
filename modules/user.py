class user_class():
    def __init__(self, username):
        self.username = username
    
    def save_user_in_cache(self):
        save = open("cache.txt", "a")
        save.write(f"{self.username}")
        save.close()
    
    def check_user_in_cache(self):
        load = open("cache.txt", "r")
        for line in load:
            if self.username in line:
                return True
        return False
    