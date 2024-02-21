-- inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server

USE hbtn_0c_0;

-- Check if the row with id 89 already exists
IF NOT EXISTS (SELECT * FROM first_table WHERE id = 89) THEN
    -- Insert the new row
    INSERT INTO first_table (id, name) VALUES (89, 'Best School');
    SELECT 'Row inserted successfully.' AS status;
ELSE
    SELECT 'Row with id 89 already exists. No insertion performed.' AS status;
END IF;
