from flaskext.mysql import MySQL


class MysqlQuery(MySQL):
    def __init__(self,app):
        super().__init__(app)
        self.init_app(app)


    def request_Data_Base(self, requete: str):
        cur = self.get_db().cursor()
        cur.execute(requete)
        data = cur.fetchall()
        cur.close()
        return data

def main():
    pass


if __name__ == '__main__':
    main()