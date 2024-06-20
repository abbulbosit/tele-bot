import psycopg2 as psql
import os


class Database:
    @staticmethod
    async def connect(query, query_type):
        db = psql.connect(
            database=os.getenv('db_name'),
            user=os.getenv('user_name'),
            password=os.getenv('user_password'),
            host=os.getenv('user_host'),
            port=os.getenv('port')
        )

        cursor = db.cursor()
        data = ["insert", "delete"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted successfully"

        else:
            return cursor.fetchall()

    @staticmethod
    async def check_user_id(user_id: int):
        query = f"SELECT * FROM users_2 WHERE user_id = {user_id}"
        check_user = await Database.connect(query, query_type="select")
        if len(check_user) == 1:
            print(">>>>>>>>>>>>>>>>", check_user)
            return True
        return False