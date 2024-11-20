/*
PostgreSQL – Subquery
Subqueries, also known as nested queries or inner queries, are queries embedded within another SQL query. They allow you to perform multiple queries within a single PostgreSQL command, making your SQL statements more powerful and efficient

What is a Subquery?
A subquery is a query nested inside another query, typically within the ‘SELECT', ‘INSERT', ‘UPDATE', or ‘DELETE' statements. Subqueries are used to perform complex data retrieval operations and can return individual values or a set of rows that the main query uses for its conditions.


Syntax:

SELECT column1, column2
FROM table1
WHERE column1 = (SELECT column1 FROM table2 WHERE condition);

*/
--Example 1: Finding Films with Rental Rates Higher than Average
--WITHOUT SUBQUERY We will find the average rental rate by using the SELECT statement and average function( AVG). Then use the result of the first query in the second SELECT statement to find the films that has higher rental rate than the average.
SELECT
    AVG (rental_rate)
FROM
    film; 
--o/p avg 2.9800000000000000 

--Now we will query for films whose rental rate is higher than the average rental rate.
SELECT
    film_id,
    title,
    rental_rate
FROM
    film
WHERE
    rental_rate > 2.98;
 
--As you can observe the above query is not too elegant and requires an unnecessary amount of multiple queries. This can be avoided by using PostgreSQL subqueries as below.

SELECT
    film_id,
    title,
    rental_rate
FROM
    film
WHERE
    rental_rate > (
        SELECT
            AVG (rental_rate)
        FROM
            film
    );
   
   
/*
Sequence of Execution:

Execute the subquery to get the average rental rate.
Pass the result to the outer query.
Execute the outer query to find films with rental rates higher than the average. 
 
 */
