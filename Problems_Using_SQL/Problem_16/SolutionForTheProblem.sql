-- Select distinct city names from the STATION table
SELECT DISTINCT city 
FROM station 
WHERE 
    -- Convert city names to lowercase and filter out names starting with vowels
    LOWER(city) NOT LIKE 'a%' 
    AND LOWER(city) NOT LIKE 'e%' 
    AND LOWER(city) NOT LIKE 'i%' 
    AND LOWER(city) NOT LIKE 'o%' 
    AND LOWER(city) NOT LIKE 'u%' 

    -- Filter out city names ending with vowels
    AND LOWER(city) NOT LIKE '%a' 
    AND LOWER(city) NOT LIKE '%e' 
    AND LOWER(city) NOT LIKE '%i' 
    AND LOWER(city) NOT LIKE '%o' 
    AND LOWER(city) NOT LIKE '%u';

