-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server
SELECT user, host, db, select_priv, insert_priv, update_priv, delete_priv, create_priv, drop_priv, grant_priv
FROM mysql.db
WHERE user IN ('user_0d_1', 'user_0d_2');

