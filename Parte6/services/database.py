import sqlite3

class MyDatabase:
    def __init__(self) -> None:
        self._db_connection = sqlite3.connect("social_network.db", check_same_thread=False)
        self._cursor = self._db_connection.cursor()
        create_post_table = "CREATE TABLE IF NOT EXISTS post (post_id text PRIMARY KEY, user_name text, content text)"
        self._cursor.execute(create_post_table)
        self._db_connection.commit()

    def create_post(self, post):
        create_post_SQL = "INSERT INTO post VALUES ('{}', '{}', '{}')".format(post.id, post.user_name, post.content)
        self._cursor.execute(create_post_SQL)
        self._db_connection.commit()

    def list_posts(self):
        list_posts_SQL = "SELECT * from post;"
        return self._cursor.execute(list_posts_SQL).fetchall()

    def delete_post(self, post):
        delete_post_SQL = "DELETE FROM post WHERE post_id='{}'".format(post.id)
        self._cursor.execute(delete_post_SQL)
        self._db_connection.commit()

    def find_post(self, post_id):
        select_post_SQL = "SELECT * FROM post WHERE post_id='{}'".format(post_id)
        return self._cursor.execute(select_post_SQL).fetchone()

    def edit_post(self, post):
        edit_post_SQL = "UPDATE post SET content='{}' WHERE post_id='{}'".format(post.content, post.id)
        self._cursor.execute(edit_post_SQL)
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()
        