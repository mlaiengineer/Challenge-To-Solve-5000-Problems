-- Calculate the total population of all cities in Asia

SELECT SUM(city.Population)  -- Summing the population of cities
FROM city
INNER JOIN country ON city.CountryCode = country.Code  -- Joining city and country tables using the country code
WHERE country.Continent = 'Asia';  -- Filtering only for countries in the Asian continent
