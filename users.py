from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated = data["updated_at"]

    @classmethod
    def get_all_users(cls):
        mysql = connectToMySQL("users")
        query = "SELECT * FROM users"
        results = mysql.query_db(query)
        res = []
        for result in results:    
            res.append(User(result))
        return res
    @classmethod
    def add_user(cls,formdata):
        mysql = connectToMySQL("users")
        query = 'INSERT INTO users VALUES(null, %(first_name)s,%(last_name)s,%(email)s,NOW(),NOW())'
        mysql = connectToMySQL('users')
        mysql.query_db(query,formdata)