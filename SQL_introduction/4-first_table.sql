-- 4-first_table.sql

USE `hbtn_test_db_4`;

-- Check if the table already exists
SET @table_exists = (
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = DATABASE() AND table_name = 'first_table'
);

-- If the table doesn't exist, create it
IF @table_exists = 0 THEN
    CREATE TABLE first_table (
        id INT,
        name VARCHAR(256)
    );
END IF;
