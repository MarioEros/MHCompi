sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                    user_id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    lang TEXT NOT NULL
                                ); """