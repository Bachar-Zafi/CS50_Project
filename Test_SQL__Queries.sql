-- SQLite

--1. to get asset VAR/FP/TIP for a user chosen year
SELECT Asset_VAR 
FROM full_table
WHERE Year = "2050";


--3. in what year was the highest asset VAR/FP/TIP reached 
SELECT Year
FROM full_table
WHERE Asset_VAR = (
        SELECT 
            MAX(Asset_VAR)
        FROM
            full_table);

