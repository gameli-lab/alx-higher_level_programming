--Thus reads a database after creating
CREATE DATABASE IF NOT EXIST hbtn_0d_2;

CREATE USER IF NOT EXIST 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0s_2.* TO 'user_0d_2'@'localhost';
