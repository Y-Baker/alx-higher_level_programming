-- creates the database hbtn_0d_2 and the user user_0d_2
-- CREATE DATA BASE
CREATE DATABASE IF NOT EXISTS  hbtn_0d_2;
-- CREATE USER
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- ADD PERMISSIONS
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
