-- 4-first_table.sql

USE `hbtn_test_db_4`;

-- Try to create the table; ignore errors if it already exists
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);