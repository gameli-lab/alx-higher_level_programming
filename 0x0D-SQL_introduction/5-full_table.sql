-- Describes a table in details
SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
FROM information_schema.schema
WHERE table_schema='hbtn_0c_0' AND table_name='first_table';
