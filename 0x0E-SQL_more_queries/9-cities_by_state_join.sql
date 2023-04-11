-- List all cities in the database
-- Select cities and state
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;
