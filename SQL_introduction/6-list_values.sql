USE hbtn_0c_0;

-- Check if the table has records
IF EXISTS (SELECT 1 FROM first_table LIMIT 1) THEN
    -- Select all rows from the first_table
    SELECT * FROM first_table;
ELSE
    -- Display a message if the table has no records
    SELECT 'Table has no records.' AS message;
END IF;