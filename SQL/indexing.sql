/*SQL INDEX - Indexing creates a separate memory location and stored column in a sorted manner and also save pointer for memory location

Syntax
CREATE INDEX index_name ON table_name [USING method]
(
    column_name [ASC | DESC] [NULLS {FIRST | LAST }],
    ...
);*/

--Create an Index- Now, let’s create an index on the last_name column to speed up queries that filter by last name.
create index idx_lastname on students(lastname);

/* Step 3: Querying with the Index-Now, when you query the Students table using the last_name column, 
the database can use the index to find records more quickly.*/

select * from students 
where lastname = 'Mane';
 --Step 4: Check the Execution Plan -To see how the index is used, you can check the execution plan. 
 --In PostgreSQL, you can use the EXPLAIN keyword: This will show you whether the index is being utilized in the query.
explain select * from students 
where lastname = 'Mane';

--Drop the Index - If you find that the index is no longer needed, you can drop it:
DROP INDEX idx_lastname;


/* Summary of Indexing
Table Creation: We created a Students table.
Index Creation: We created an index on the last_name column.
Query Execution: We ran a query that benefits from the index.
Execution Plan: We checked the execution plan to verify index usage.
Dropping the Index: We removed the index if it was no longer needed.
*/



Example-2
/*Why Use Indexes?
Indexes in PostgreSQL organize table data in a particular order to speed up searches. 
They act like the alphabetized phone book, allowing for quick data retrieval. 
Without indexes, PostgreSQL performs a sequential scan, checking each row until it finds the matching data. 
This method is slow, especially for large datasets.*/

SELECT * FROM address
WHERE phone = '223664661973';

EXPLAIN SELECT * FROM address
WHERE phone = '223664661973';

CREATE INDEX idx_address_phone 
ON address(phone);

EXPLAIN SELECT * FROM address
WHERE phone = '223664661973';

