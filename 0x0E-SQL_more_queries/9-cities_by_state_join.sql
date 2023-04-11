-- List all cities in the database
-- Select cities and state
SELECT cities.id, cities.name, states.name
FROM cities
JOIN ON states WHERE cities.state_id = state.id;
