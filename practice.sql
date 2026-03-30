-- code 1: Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
--The STATION table is described as follows:
--SELECT count(CITY)- count(distinct CITY) FROM STATION;

--code 2: Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
--The STATION table is described as follows:
-- (SELECT CITY,LENGTH(CITY) as city_length FROM STATION ORDER BY
--LENGTH(CITY),CITY limit 1) UNION (SELECT CITY,LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY)DESC,CITY limit 1);