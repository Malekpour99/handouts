-- Creating a database
CREATE DATABASE your_database_name;

-- PostgreSQL database does not support ENUM so we need to define a custom type to be able to choose among specific entries
CREATE TYPE custom_type AS ENUM('value1', 'value2', 'value3');

-- If you must have a keyword name as your table name put it between double quotes ("")
-- Creating a table with specified fields & types
CREATE TABLE your_table_name (
    id SERIAL PRIMARY KEY, -- SERIAL will create an INTEGER and do the auto increment action in PostgreSQL
    -- PRIMARY KEY is the combination of 'UNIQUE' and 'NOT NULL' constraints and each table can only
    -- have one primary key column
    PRIMARY KEY (column_1, column_2), -- composite PRIMARY KEY, can also be defined with this syntax!
    column_1 VARCHAR(255) NOT NULL,
    column_2 INTEGER CHECK (column_2 >= 0),
    column_3 custom_type,
    column_4 FLOAT,
    column_5 NUMERIC(6, 2), -- (total digits, decimal digits)
    column_6 BOOLEAN DEFAULT TRUE,
    column_7 TEXT,
    column_8 TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    column_9 DATE DEFAULT (CURRENT_DATE),
    -- Creating Foreign Keys + constraints
    column_10_1 INTEGER REFERENCES other_table_name (column_name) ON DELETE CASCADE,
    column_10_2 INTEGER REFERENCES other_table_name ON DELETE SET NULL, -- if you don't mention the column_name the 'primary key' will be considered
    column_10_3 INTEGER REFERENCES other_table_name (column_name) ON DELETE SET DEFAULT,
    column_10_4 INTEGER REFERENCES other_table_name (column_name) ON DELETE RESTRICT,
    column_10_5 INTEGER REFERENCES other_table_name (column_name) ON UPDATE NO ACTION, -- NO ACTION is default
    FOREIGN KEY (column_10) REFERENCES other_table_name (column_name) ON DELETE SET NULL, -- is the same as below!
    column_10 INTEGER REFERENCES other_table_name (column_name) ON DELETE SET NULL, -- is the same as above!
    FOREIGN KEY (column_1, column_2) REFERENCES other_table_name (column_name_1, column_name_2), -- composite FOREIGN KEY
    -- You can use self-referencing to create foreign keys in a table which has a self-referencing relationship with a column inside that table!
    -- syntax is the same as above for defining self-referencing foreign keys and 
    -- you can also create an intermediate table for self-referencing many-to-many relationships!
    CHECK(column_5 > column_4) -- A general check for the whole table
);
-- You can also create 'TEMPORARY' tables or tables based on other tables data (by selecting you required data from them)!

-- Deleting a table
DROP TABLE your_table_name;

-- Altering a table (PostgreSQL)
ALTER TABLE your_table_name
ADD COLUMN column_0 SERIAL PRIMARY KEY, -- adding new column for id
ALTER COLUMN column_2 SET NOT NULL, -- avoiding submission of null values
ALTER COLUMN column_5 SET DATA TYPE FLOAT, -- changing data type
ALTER COLUMN column_6 SET DEFAULT FALSE, -- setting a default value
ALTER COLUMN column_1 DROP NOT NULL, -- removing a constraint
ADD CONSTRAINT constraint_name CHECK (column_4 > 0); -- adding a general constraint for table

-- Inserting data into table
INSERT INTO your_table_name (column_2, column_1, column_3, column_8)
VALUES (19000, 'Joe Nave', 'value2', '2021-10-15 16:32:10');
-- You can insert multiple values separated by commas (,) or even query your inserting values using SELECT

-- Updating data in table
UPDATE table_name 
SET column_names = new_values -- comma (,) separated if there were multiple columns
WHERE condition; -- e.g. id = n

-- Deleting data from table
DELETE FROM table_name
WHERE condition; -- deletes all rows which meet with the condition


-- Reading/Retrieving data from table
SELECT * FROM table_name; -- selecting all columns
SELECT column_names FROM table_name;
-- you can use AS keyword for renaming column names 'just' in the result set. e.g. volume AS amount (alias)
-- you can apply arithmetic actions to columns which only changes the result set shown (+ - * /) e.g. salary / 1000
-- you can also combine both of them: e.g. sales / 1000 AS total_sales

-- considering condition for filtering data (IS, =, <>, !=, IS NOT, <, <=, >, >=, AND, OR, BETWEEN)
SELECT column_names FROM table_name WHERE condition;
-- e.g. SELECT * FROM table_name WHERE date IS BETWEEN '2021-01-01' AND '2022-01-01'; (both ends are included!)

-- When you subtract two timestamps from each other the result will be in hours, minutes and ...
-- but you can convert the result like this: WHERE EXTRACT(DAY FROM date_finished - date_started) <= 5;
-- now the comparison happens using days difference between the two timestamps

-- considering a specific order for sorting data (order comes after where conditions)
SELECT column_names FROM table_name ORDER BY column_names DESC; -- separate column names for ordering using comma (,)
-- default ordering happens in ascending order (ASC) but by using DESC keyword you can get a descending order

-- limiting number of result set (limiting comes after ordering)
SELECT column_names FROM table_name LIMIT number_of_results;
-- you can also select a certain number of results after skipping a certain number:
SELECT column_names FROM table_name LIMIT number_of_results OFFSET number_of_offsets;

-- selecting unique results (removes duplicates)
SELECT DISTINCT column_names FROM table_name;

-- using sub-queries for reading data
SELECT column_names FROM (SELECT column_names FROM table_name WHERE condition) AS sub_query_name;
-- further about this later!

-- you can create VIEWs from frequently used sub-queries
CREATE VIEW base_query_name AS SELECT column_names FROM table_name WHERE condition;
-- using VIEW for reading data (it can also be used for inserting data into tables)
SELECT * FROM base_query_name WHERE condition;


-- Normalization Simple Rules:
-- 1- Avoid mixing data entities in the same table!
-- 2- Avoid storing multiple values in a single table cell!
-- 3- Avoid splitting simple data across multiple tables!

-- INNER JOIN (JOIN) tables
SELECT column_names 
FROM your_table_name_1 AS t1 
INNER JOIN your_table_name_2 AS t2 
ON t1.column_id = t2.column_id;

-- Stacking table joins + filtering result set
SELECT column_names 
FROM your_table_name_1 AS t1 
INNER JOIN your_table_name_2 AS t2 
ON t1.column_id = t2.column_id
INNER JOIN your_table_name_3 AS t3
ON t2.column_id = t3.column_id
WHERE condition;
-- You can also apply ordering and limiting on the result set

-- LEFT JOIN (LEFT OUTER JOIN) tables
-- Left join considers all the data from the left result set 
-- (table/tables which we select from and join on)
-- and returns all the data even if there are no matching rows
SELECT column_names 
FROM your_table_name_1 AS t1 
LEFT JOIN your_table_name_2 AS t2 
ON t1.column_id = t2.column_id;
-- You can also combine left joins but keep in mind that the result of
-- the previous left join will be passed to the next left join

-- RIGHT JOIN is also available but since every right join can actually be
-- a left join, it's not very common to use right join!

-- CROSS JOIN (won't be used too often!!)
-- Returns all of the possible combinations 
-- between the first table rows with the second table rows
SELECT column_names
FROM your_table_name_1
CROSS JOIN my_table_name_2;

-- UNION Vs. JOIN
-- Union: combines multiple result sets into one result set by appending rows
-- Join: merges multiple tables into one result set by appending columns

-- UNION (Useful for tables with identical columns)
SELECT ...
UNION
SELECT ...;
-- column counts between select statements must be identical!!

-- Relations
-- 1:1 (one to one) --> create column in either of tables which makes more sense
-- 1:n (one to many) --> create column in the 'many' table which can include only one data per cell
-- n:n (many to many) --> create an 'intermediate' table for managing relations using tables primary keys

-- Aggregate Functions
SELECT SUM(column) FROM table_name; -- Returns total sum of the column values
SELECT COUNT(*) FROM table_name; -- Returns total count of the table rows
-- when you specify a column for count, it doesn't count NULL values!
SELECT COUNT(DISTINCT column) FROM table_name; -- Returns total count of unique values
SELECT MAX(column) FROM table_name; -- Returns the maximum of the column values
SELECT MIN(column) FROM table_name; -- Returns the minimum of the column values
SELECT AVG(column) FROM table_name WHERE condition; -- Returns the average of the column values
-- average doesn't consider NULL values!
SELECT ROUND(AVG(column),2) FROM table_name WHERE condition; -- Returns the rounded average of the column values with only 2 decimal places
-- You can also select multiple aggregated values by separating them by commas (,).

-- Combining aggregate functions with non-aggregate identifiers
-- for this purpose you must use GROUP BY!
SELECT column_name, SUM(column)
FROM table_name
GROUP BY column_name; -- you can also use GROUP BY to group result set for multiple columns (separated by commas)
-- The result set is grouped by the column_name and the sum related to that group is returned in front of it. (without duplicates)

-- For filtering aggregate functions you can use HAVING filter which applies after the GROUP BY clause
-- but WHERE clause apply before the GROUP BY clause
SELECT column_name, COUNT(column)
FROM table_name
GROUP BY column_name
HAVING SUM(column) > n; -- Now the count result only considers rows that have the SUM higher than the specified amount 'n' 
-- Summary: 
-- 1- WHERE applies on the raw data where the HAVING applies on the aggregated data!!
-- 2- WHERE doesn't accept aggregate function as the condition where the HAVING also accepts aggregate functions as the condition!!

-- Nested Sub-Queries
SELECT ... 
FROM (
    another_select_query
) AS sub_query_name;
-- e.g.
SELECT booking_date
FROM bookings
GROUP BY booking_date
HAVING SUM(amount_billed) = (
    SELECT MIN(daily_sum)
    FROM (
        SELECT booking_date, SUM(amount_billed) AS daily_sum
        FROM bookings
        GROUP BY booking_date
    ) AS daily_table
);
-- finding the date in which the total sum of bill amounts is the minimum!


-- Window Functions (allows you to use aggregate functions along with other data)
-- e.g.
SELECT booking_date, amount_tipped, SUM(amount_tipped) OVER()
FROM bookings; -- Adds the total amount of tips next to each row!
SELECT booking_date, amount_tipped, SUM(amount_tipped) OVER(PARTITION BY booking_date)
FROM bookings; -- Groups the result of total amount of tips based on the date but shows that date's sum of tips along with other rows
-- next to each data and tip amount data without removing any data!

-- Ranking and sorting data in the window function
SELECT booking_date, amount_tipped, RANK() -- Gives a rank to each row
OVER(PARTITION BY booking_date ORDER BY amount_tipped DESC)
FROM bookings; -- Groups the result of total amount of tips based on the date but shows that date's sum of tips along with other rows

-- Arithmetic functions
CEIL() -- Returns the ceiling of a decimal number by rounding up the number
FLOOR() -- Returns the floor of a decimal number by rounding down the number
ROUND( , n) -- Returns a rounded number by 'n' based on its decimal values
TRUNC( , n) -- Returns a number with 'n' decimal values and cuts the other decimal values

-- String functions
CONCAT(first_name, ' ', last_name) -- Concats the given strings
SELECT first_name || ' ' || last_name -- Concats the given strings only for Postgres
UPPER() -- Converts all the strings letters to upper-case
LOWER() -- Converts all the strings letters to lower-case
WHERE LENGTH(column) > n; -- Returns all the strings which has more than n characters
TRIM(LEADING ' ' data_value) -- Trims the  given character(s) - in this case spaces - from the mentioned position
TRIM(TRAILING ' 'data_value) -- Trims the  given character(s) - in this case spaces - from the mentioned position
TRIM(BOTH ' ' data_value) -- Trims the  given character(s) - in this case spaces - from the mentioned position

-- Date functions
EXTRACT(MONTH FROM date_column) -- Extracts month from the date value in the column
EXTRACT(YEAR FROM date_column) -- Extracts year from the date value in the column
EXTRACT(DAY FROM date_column) -- Extracts day from the date value in the column
EXTRACT(MINUTE FROM date_column) -- Extracts minute from the date value in the column
date_column::TIMESTAMP::DATE -- Only shows the date part of the timestamp column
date_column::TIMESTAMP::TIME -- Only shows the time part of the timestamp column
-- Below functions work only in PostgreSQL and is different in MySQL!!
EXTRACT(DOW FROM date_column) -- Extracts day of the week from the date value in the column (sun=0, mon=1, ..., sat=6)
EXTRACT(ISODOW FROM date_column) -- Extracts day of the week from the date value in the column (mon=1, ..., sat=7)

-- Intervals and date differences
date_column_1 - date_column_2 -- Returns an 'interval' result for timestamps and 'days' for dates
NOW() - date_column_1 -- Returns the difference between the current date and the column date as an 'interval'
date_column_1 + 7 -- Adds 7 days to the date data in the column
date_column_1 + INTERVAL '7 MONTH' -- Adds 7 months to the date data in the column but returns a timestamp as a result
(date_column_1 + INTERVAL '7 YEARS')::TIMESTAMP::DATE -- Adds 7 years to the date data in the column but we convert the timestamp to a date

-- LIKE & Pattern matching
SELECT first_name LIKE 'max' ... -- Looks for exact matches 
SELECT first_name LIKE 'ma%' ... -- Looks for matches which start with 'ma' and leading to unknown number of characters
SELECT first_name LIKE '%a%' ... -- Looks for matches which has 'a' in their characters (LIKE is case-sensitive)
SELECT first_name ILIKE '%a%' ... -- Looks for matches which has 'a' in their characters (ILIKE is case-insensitive)
SELECT first_name 
FROM your_table_name
WHERE first_name LIKE '_a%'; -- Looks for matches which has 'a' in their characters and exactly one character before 'a'
-- Returns boolean values as the result set for each row (PostgreSQL)!

-- Sub-Queries & Exists
SELECT EXISTS (
    SELECT column_name
    FROM table_names
    WHERE condition
); -- Returns TRUE or FALSE as the result

-- Instead of joining tables, we can use sub-queries for our results
SELECT t.column_name
FROM table_names AS t
WHERE EXISTS (
    SELECT a.column_name
    FROM another_table_name AS a
    WHERE t.id = a.id AND condition
);

-- checking a condition with the help of an array
SELECT column_name
FROM table_name
WHERE column_name IN('value_1', 'value_2')
-- instead of this:
SELECT column_name
FROM table_name
WHERE column_name = 'value_1' OR column_name = 'value_2';
-- you can also use NOT IN for checking a condition

-- Conditional Expression
SELECT income_column
    CASE WHEN income_column >= 1000 THEN 'Good Day'
         WHEN income_column > 500
         ELSE 'Bad Day'
    END -- Orders matter in the condition cases otherwise define your conditions with more details
FROM table_name;

-- Practical Example for days of the week
SELECT week_day
    CASE 
        WHEN week_day = '1' THEN 'Monday'
        WHEN week_day = '2' THEN 'Tuesday'
        WHEN week_day = '3' THEN 'Wednesday'
        WHEN week_day = '4' THEN 'Thursday'
        WHEN week_day = '5' THEN 'Friday'
        WHEN week_day = '6' THEN 'Saturday'
        ELSE 'Sunday'
    END
FROM (
    SELECT DOW FROM date_column
    FROM table_name
) AS weekday_numbers;

-- Transaction for managing execution of multiple queries
-- PostgreSQL has built-in transaction session in VS-Code when running its commands!!!
-- Transaction SQL file
BEGIN; -- Converts the current connection session to a transaction (PostgreSQL)

-- Query SQL file-1
...

SAVEPOINT savepoint_name; -- By creating a savepoint now the rollback action will return here instead of removing all the changes!!

-- Query SQL file-2
...

-- Rollback SQL file
ROLLBACK; -- Rolling back all the changes applied in the current session and terminating the transaction
ROLLBACK TO savepoint_name; -- Rolling back all the changes applied after the savepoint (keeps the transaction)
-- Commit SQL file
COMMIT; -- Committing changes applied in the current session and terminating the transaction
-- There are actions which can lead to an implicit commit (like starting a new session without terminating the previous one)
-- Read more about this in the official documentation

-- Indexes help to enhance our query performance especially when we have a condition
-- by using indexes values are sorted in an extra table which is connected to the original table and helps with running queries more efficiently
-- Don't use too many indexes or index every column this might even worsen your performance cause
-- if you have many indexes or frequent changes of data you must update both the original table and the index table.

-- For more information about different type of indexes you can read the official documentation (Technical Implementation e.g. B-Tree, Hash, ...)

-- Functionality of indexes:
--  standard single-column index
--  unique index
--  multi-column index
--  Partial index

EXPLAIN
SELECT * FROM your_table_name WHERE condition;
-- Explains about the performance and execution of your query

EXPLAIN ANALYZE
SELECT * FROM your_table_name WHERE condition;
-- Explains about the performance and execution of your query and also returns the analysis of the execution

-- Creating a single-column index
CREATE INDEX index_name ON table_name (column_name); -- Creates an index on the specified column of your desired table

-- Creating a unique index
CREATE UNIQUE INDEX index_name ON table_name (column_name); -- Creates a unique index on the specified column of your desired table
-- By adding 'UNIQUE' constraint to a column when creating a new table, an index will be created for that column!

-- Creating a multi-column index
CREATE INDEX index_name ON table_name (street, city, ...); -- Creates an index on the specified columns of your desired table
-- multi-column indexing is mostly used when you have 'AND' between your filtering conditions
-- The order of the columns matter cause you can still use this index as a single-column index for filtering the results of the first mentioned column; or
-- when you have more than two columns you can still use the combination of the first two(/three, ...) columns to benefit from multi-column indexes in your filtering

-- Creating partial index (not available in MySQL)
CREATE INDEX index_name ON table_name (column_name)
WHERE column_name >= some_value; -- Creates a partial index on the specified column of your desired table

-- Removing an index
DROP INDEX index_name;
