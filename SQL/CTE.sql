/* Common Table Expressions (CTEs) in PostgreSQL are a powerful feature that allows you to define TEMPORARY RESULT sets that can be referenced within another SQL statement, such as SELECT, INSERT, UPDATE, or DELETE. CTEs are temporary in the sense that they only exist during the execution of the query. They are typically used to simplify complex joins and subqueries, 
making your SQL code more readable and maintainable.



Syntax
WITH cte_name (column_list) AS (
    CTE_query_definition
)
statement;


Let’s analyze the above syntax.

CTE Name: The first step is to set the name of the CTE, followed by an optional column list.
CTE Query Definition: Specify a query that returns the result set within the body of the WITH clause. If the column list is not specified, the select list of the CTE_query_definition will become the column list of the CTE.
Usage: Finally, use the CTE like a table or view in the statement, which can be a SELECT, INSERT, UPDATE, or DELETE.

PostgreSQL CTE Examples

In this example, we will define a CTE named cte_film using the WITH clause with the film table. We will categorize films based on their length as ‘Short’, ‘Medium’, or ‘Long’.

*/
WITH cte_film AS (
    SELECT 
        film_id, 
        title,
        (CASE 
            WHEN length < 30 THEN 'Short'
            WHEN length < 90 THEN 'Medium'
            ELSE 'Long'
        END) length    
    FROM
        film
)
SELECT
    film_id,
    title,
    length
FROM 
    cte_film
WHERE
    length = 'Long'
ORDER BY 
    title;