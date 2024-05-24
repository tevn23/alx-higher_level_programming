-- Lists all cities in the USA database
SELECT cities.id, cities.name, states.name
FROM cities, state_id
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
