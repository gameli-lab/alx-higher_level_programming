-- Moving to utf8
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256),
    score INT
);


ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
