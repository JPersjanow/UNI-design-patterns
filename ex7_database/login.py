class DBLogin:
    def __init__(self, dbname, password):
        self.dbname = dbname
        self.password = password

    def check_password(self) -> bool:
        if self.password == f'{self.dbname}_pass':
            return True
        else:
            return False