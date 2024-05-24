-- Lists all cities in the USA database
SELECT c.id, c.name, c.name
FROM cities AS c
INNER JOIN states AS s
ON c.state_id = s.id 
ORDER BY c.id ASC;
