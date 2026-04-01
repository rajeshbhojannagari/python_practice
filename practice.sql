-- code 1: Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
--The STATION table is described as follows:
--SELECT count(CITY)- count(distinct CITY) FROM STATION;

--code 2: Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
--The STATION table is described as follows:
-- (SELECT CITY,LENGTH(CITY) as city_length FROM STATION ORDER BY
--LENGTH(CITY),CITY limit 1) UNION (SELECT CITY,LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY)DESC,CITY limit 1);

--code 3: Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
--SELECT DISTINCT CITY FROM STATION WHERE CITY like 'a%'or CITY like'e%' or CITY like 'i%' or CITY like 'o%' or CITY like 'u%';

--code 4: Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
--SELECT DISTINCT CITY FROM STATION WHERE CITY like '%a'or CITY like'%e' or CITY like '%i' or CITY like '%o' or CITY like '%u';

--code 5: Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
--SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU].*[AEIOU]$';

--code 6: Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
--SELECT DISTINCT CITY FROM STATION WHERE CITY not like 'a%' and CITY not like 'e%' AND CITY not like 'i%' and CITY not like 'o%' and CITY not like 'u%';

--code 7: Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
--SELECT DISTINCT CITY FROM STATION WHERE CITY not like '%a' and CITY not like '%e' AND CITY not like '%i' and CITY not like '%o' and CITY not like '%u';

--code 8: Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
--SELECT DISTINCT CITY from STATION WHERE CITY NOT  REGEXP '^[AEIOU].*[AEIOU]$';

--code 9: Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
--SELECT DISTINCT CITY FROM STATION WHERE CITY not REGEXP '^[AEIOU].' AND CITY not REGEXP '[AEIOU]$';

--code 10: Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
--SELECT Name FROM STUDENTS WHERE Marks>75 ORDER BY Right(Name,3) ,ID ASC; 

--code 11: Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
--SELECT name FROM Employee order by name asc;