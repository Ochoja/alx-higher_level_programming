-- List rows in a database
-- List cities with state_id = 1
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name='California')
SORT BY id ASC;
