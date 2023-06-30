SELECT Country.continent, FLOOR(AVG(City.population)) 
FROM City 
INNER JOIN Country 
ON City.countrycode = Country.code 
GROUP BY Country.continent;