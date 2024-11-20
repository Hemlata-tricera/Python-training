--To select particular columns we can name the columns:

select customer_id, store_id from customer;

--If we want all of the columns, we can use * as shorthand:

SELECT * FROM customer;

--The WHERE clause is used to filter records.
--It is used to extract only those records that fulfill a specified condition.

select * from customer where store_id=2;

--You can combine conditions together with AND and OR:
select * from customer c where customer_id=400 and store_id=2;

--Note that string (text) values in SQL are surrounded with single quotes:

select * from staff where first_name='Jon';

--with WHERE operators
select * from staff where first_name != 'Jon';

select * from staff where first_name <> 'Jon';
--Exercises Select rows from the film table where the film_id is less than 4.
select * from film where film_id < 4;

-- Select rows from the film table where the rating is PG.
select * from film f where rating = 'PG';

--Select rows from the film table where the rating is PG or G.
select * from film f where rating = 'PG' or rating = 'G';



--BETWEEN is shorthand for # <= x <= #. The endpoints are inclusive:

select * from film where film_id between 1 and 5;

--IN lets you specify a lot of values that you would otherwise join together with an OR statement:

select * from film where film_id in (3,5,7,9);

--Exercise Select rows from the actor table where the first name is Angela, Angelina, or Audrey using IN.
select * from actor where first_name in ('Angela', 'Angelina', 'Audrey');

--ORDER BY - The ORDER BY keyword is used to sort the result-set in ascending or descending order.
--By default, sorting is done in ascending (ASC) order.
select film_id, title from film order by film_id;

--To get the reverse order of sorting, use DESC (descending):
select film_id, title from film order by film_id desc;


--DISTINCT removes duplicate rows from the result. It comes before the list of column names, and applies to the combination of all columns.

select distinct customer_id, staff_id from payment;
select customer_id, staff_id from payment;


--SQL NOT Operator
--The NOT operator is used in combination with other operators to give the opposite result, also called the negative result.

select * from film where not rating = 'PG';

--NOT LIKE
select * from actor where first_name not like 'J%';
--NOT BETWEEN
select * from film where film_id not between 1 and 5;
--NOT IN
select * from film where film_id not in (3,5,7,9,155);
--NOT Greater Than
select * from film where not film_id > 4; 






select distinct film_id from film where film_id <= 4;
--*********************************************************************************

--Note: There is a not-greater-than operator: !> that would give you the same result.

select * from film where film_id !> 4; --NOT WORKING



--***********************************************************************
select * from film where not film_id < 4;





--NULL Values
select address_id, address, address2 from address 
where address2 is null;


select address_id, address, address2 from address 
where address2 is not null;  


select * from actor;

update actor
set first_name = 'Jayesh'
where actor_id = 1;

--UPDATE Multiple Records

update actor
set first_name = 'Vivek'
where last_name = 'Bergen';

***********************************************************
--The SQL SELECT TOP Clause
select top 3 * from actor ;
******************************************************************
--LIMIT
select * from actor
limit 30;

--FETCH FIRST
select * from actor
fetch first 3 rows only;
****************************************************************
--SQL TOP PERCENT Example
select top 50 percent from actor;
****************************************************************
*****************************************************************
--ADD a WHERE CLAUSE

select top 3* from city
where country_id = 44;
**********************************************************************

select * from city 
where country_id = 44
limit 3 offset 1;

select * from city
where country_id = 44
fetch first 3 rows only ;

--ADD the ORDER BY Keyword
--Add the ORDER BY keyword when you want to sort the result, and return the first 3 records of the sorted result.
select * from city 
order by city desc
limit 3;

--The following SQL statement shows the equivalent example for Oracle:
select * from city 
order by city desc
fetch first 3 rows only;


--SQL Aggregate Functions
--The MIN() function returns the smallest value of the selected column.

select min(amount)
from payment;

--The MAX() function returns the largest value of the selected column.

select max(amount) from payment;

--Set Column Name (Alias)
--When you use MIN() or MAX(), the returned column will not have a descriptive name. To give the column a descriptive name, use the AS keyword:
select min(amount) as SmallestAmount from payment;


--Use MIN() with GROUP BY
select * from payment;


select min(amount) as SmallestPrice, customer_id from payment
group by customer_id ;


--SQL COUNT() Function
--The COUNT() function returns the number of rows that matches a specified criterion.
select count(*) from  actor;
--Specify Column You can specify a column name instead of the asterix symbol (*). NULL values will not be counted.
select * from actor;
select count(first_name) from actor; 
--Add a WHERE Clause
select count(first_name) from actor 
where actor_id > 20;

--Ignore Duplicates
select count(distinct actor_id) from actor;

--Use an Alias
select count(*) as Number_of_Re
from actor;


--SQL SUM() Function
select * from city

select sum(city_id) from city;

--Add a WHERE Clause
select sum(city_id) from city where country_id = 82;

--SUM() With an Expression
select sum(city_id * 10) from city;

--SQL AVG() Function

select avg(city_id) from city;

select * from payment 

select avg(amount) from payment; 

select avg(amount) from payment where customer_id = 341;

--Use an Alias
select avg(amount) as average_price from payment;
--Higher Than Average
select * from payment 
where amount > (select avg(amount) from payment);

--Use AVG() with GROUP BY
select avg(amount) from payment group by staff_id; 

--SQL LIKE Operator

select * from city where city like 'D%';

select * from city where city like 'A%';

--The _ Wildcard

select * from city where city like 'A_u_';

--The % Wildcard
select * from city where city like '%A%';

select * from city where city like '%B%';
--Starts With
--To return records that starts with a specific letter or phrase, add the % at the end of the letter or phrase.
select * from city where city like 'Ah%'

--Ends with
--To return records that ends with a specific letter or phrase, add the % at the beginning of the letter or phrase.

select * from city where city like '%h'

--Contains
--To return records that contains a specific letter or phrase, add the % both before and after the letter or phrase.
select * from city where city like '%ta%'

--Combine Wildcards
--Any wildcard, like % and _ , can be used in combination with other wildcards.
select * from city where city like 'a__%';

--Return all customers that have "r" in the second position:

select * from city where city like '_r%';

--Without Wildcard- If no wildcard is specified, the phrase has to have an exact match to return a result.
select * from city where city like 'Brest';


--SQL Wildcard Characters
A wildcard character is used to substitute one or more characters in a string.

select * from city where city like '[ABC]%';
select * from city where city like '[A-G]%';



--The SQL IN Operator-> The IN operator allows you to specify multiple values in a WHERE clause.
select * from city;
select * from city where city in ('Acua', 'Bhusawal', 'Jaipur');

--NOT IN By using the NOT keyword in front of the IN operator, you return all records that are NOT any of the values in the list.
select * from city where city not in ('Acua', 'Bhusawal', 'Jaipur');


--SQL Aliases
--In PostgreSQL, square brackets ([]) are not used for aliases; instead, you should use double quotes ("") 
--if you want to include spaces or special characters in your alias. Here's how you would write your query:
SELECT city AS "City Name"
FROM city;


--AS is Optional-> Actually, in most database languages, you can skip the AS keyword and get the same result:
SELECT city "City Name"
FROM city;

--The SQL BETWEEN Operator
SELECT * FROM customer
WHERE customer_id BETWEEN 10 AND 20;

--NOT BETWEEN
SELECT * FROM customer
WHERE customer_id not BETWEEN 10 AND 20;

--Alias for Columns
select customer_id as ID, first_name as CustomerName from customer;

--SQL JOIN A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
--SQL INNER JOIN
--The INNER JOIN keyword selects records that have matching values in both tables.
select * from film_category
select * from category 
select * from payment p
inner join customer  c on p.customer_id = c.customer_id 

select * from film_category fc 
inner join category c2 
on fc.category_id = c2.category_id 

select * from film_category fc 
left join category c2 
on c2.category_id=  fc.category_id

select * from film_category fc 
right join category c2 
on fc.category_id = c2.category_id 

select * from film_category fc 
full join category c2 
on fc.category_id = c2.category_id 


--Create New table student

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,  -- Primary Key
    Email VARCHAR(255) UNIQUE,  -- Unique Key
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    CourseID INT,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)  -- Foreign Key
);

--Create New table Courses

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,          -- Primary Key
    CourseName VARCHAR(255) NOT NULL,  -- Course name, cannot be NULL
    Credits INT                        -- Number of credits for the course
);



insert into courses values
('101', 'BCA', 40),
('102', 'BBA', 50),
('103', 'BBM', 45),
('201', 'MCA', 60),
('202', 'MBA', 55),
('203', 'MBM', 60);

select * from courses;

insert into students values
(1, 'sunil@gmail.com', 'Sunil', 'Shrivastava', 101),
(2, 'Anil@gmail.com', 'Anil', 'Shrivastava', 102),
(3, 'swapnil@gmail.com', 'Swapnil', 'Patil', 103),
(4, 'jayesh@gmail.com', 'Jayesh', 'Shirsath', 101),
(5, 'mansi@gmail.com', 'Mansi', 'Chajed', 102),
(6, 'Sunanda@gmail.com', 'Sunanda', 'Palkonda', 103),
(8, 'Vrushali@gmail.com', 'Vrushali', 'Mane', 201),
(9, 'Suyash@gmail.com', 'Suyash', 'Pawara', 203),
(10, 'yogita@gmail.com', 'Yogita', 'Mali', 202);

select * from students 

--(INNER) JOIN: Returns records that have matching values in both tables
select s.studentid, s.firstname, s.courseid from students s
inner join courses c
on s.CourseID  = c.CourseID ;


SELECT s.StudentID, s.FirstName, s.CourseID
FROM Students s
INNER JOIN Courses c ON s.CourseID = c.CourseID;

--LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
SELECT * FROM Students s
LEFT JOIN Courses c ON s.CourseID = c.CourseID;

--RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
SELECT * FROM Students s
RIGHT JOIN Courses c ON s.CourseID = c.CourseID;

--FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
SELECT * FROM Students s
FULL JOIN Courses c ON s.CourseID = c.CourseID;

---self join*****

select s1.firstname as studentname1, s2.firstname as studentname2 
from students s1, students s2 
where s1.studentid <> s2.studentid 
and s1.lastname = s2.lastname 
order by s1.lastname 


select s1.firstname as "Student Name", s2.firstname as "TeacherName" from students s1 join students s2
on s2.studentid  = s1.studentid 

insert into students(studentid, email, firstname)values
(16, 'sushlai@gmail.com', 'Sushiila' ),
(7, 'mushi@gmail.com', 'Mushila');


select * from courses c2  

select fa.actor_id as "Actor", fa2.actor_id as "Actor Name" from film_actor fa join film_actor fa2 
on fa2.actor_id = fa.actor_id;


--CROSS JOIN- A cross join is also known as cartesian join, is a join operation that produces the cartesian product of two or more tables
--It combines each row from first table with every row of second table, resulting in a new table with a combination of all possible pairs of rows

select * from students;
select * from courses;
select * from students cross join courses 


select * from students cross join courses 
where studentid in (1,3)
order by studentid 


--Creating table for cross join with multiple tables
CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY,      -- Primary Key
    FirstName VARCHAR(100) NOT NULL,   -- First name, cannot be NULL
    LastName VARCHAR(100) NOT NULL,    -- Last name, cannot be NULL
    Email VARCHAR(255) UNIQUE,         -- Email address, must be unique
    Department VARCHAR(100)            -- Department where the instructor works
);

INSERT INTO Instructors (InstructorID, FirstName, LastName, Email, Department) VALUES
(1, 'Alice', 'Smith', 'alice.smith@example.com', 'Computer Science'),
(2, 'Bob', 'Johnson', 'bob.johnson@example.com', 'Mathematics'),
(3, 'Charlie', 'Brown', 'charlie.brown@example.com', 'Physics'),
(4, 'David', 'Williams', 'david.williams@example.com', 'Chemistry'),
(5, 'Eve', 'Davis', 'eve.davis@example.com', 'Biology'),
(6, 'Frank', 'Miller', 'frank.miller@example.com', 'History'),
(7, 'Grace', 'Wilson', 'grace.wilson@example.com', 'English'),
(8, 'Hannah', 'Moore', 'hannah.moore@example.com', 'Art'),
(9, 'Ivy', 'Taylor', 'ivy.taylor@example.com', 'Philosophy'),
(10, 'Jack', 'Anderson', 'jack.anderson@example.com', 'Economics');

select * from instructors i 


--CROSS JOIN WITH MULTIPLE TABLES
SELECT *
FROM Students
CROSS JOIN Courses
CROSS JOIN Instructors;

--UNION- The UNION operator is used to combine the result-set of two or more SELECT statements.
--Every SELECT statement within UNION must have the same number of columns
--The columns must also have similar data types
--The columns in every SELECT statement must also be in the same order

SELECT last_name FROM actor a2 
UNION
SELECT lastname FROM students s2
ORDER BY last_name ;

SELECT last_name FROM actor a2 
union ALL
SELECT lastname FROM students s2
ORDER BY last_name ;

--SQL GROUP BY Statement
--The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of students in each course".
--it is often used with aggregate functions (COUNT(), MAX(), MIN(), SUM(), AVG()) to group the result-set by one or more columns.

--GROUP BY example on students table
select * from students s2 ;
SELECT COUNT(studentid), courseid
FROM students
GROUP BY courseid
order by courseid;

--GROUP BY example on payment table
select count(payment_id), customer_id
from payment
group by customer_id 
order by count(customer_id) desc 



select * from courses;

SELECT COUNT(s.StudentID) AS StudentCount, c.CourseID, c.coursename 
FROM Students s
FULL JOIN Courses c ON s.CourseID = c.CourseID
GROUP BY c.CourseID;


--SQL HAVING Clause
--The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.

SELECT count(studentid), courseid
FROM students
GROUP BY courseid 
HAVING COUNT(studentid) > 2;


--SQL EXISTS Operator
--The EXISTS operator is used to test for the existence of any record in a subquery.
--The EXISTS operator returns TRUE if the subquery returns one or more records.

select * from students s2;
select * from courses;

SELECT firstname 
FROM students s
WHERE EXISTS (
    SELECT *
    FROM courses c
    WHERE c.courseid = s.courseid 
);

SELECT firstname 
FROM students s
WHERE not EXISTS (
    SELECT *
    FROM courses c
    WHERE c.courseid = s.courseid 
);

--SQL ANY and ALL Operators
--The ANY and ALL operators allow you to perform a comparison between a single column value and a range of other values.
select * from courses c ;
select * from students s ;

SELECT firstname
FROM students 
WHERE courseid = ANY (
    SELECT courseid 
    FROM courses 
    WHERE credits = 45
);

--Note: The operator must be a standard comparison operator (=, <>, !=, >, >=, <, or <=).
SELECT firstname
FROM students 
WHERE courseid = ANY (
    SELECT courseid 
    FROM courses 
    WHERE credits > 55
);

--The SQL ALL Operator
--returns a boolean value as a result, returns TRUE if ALL of the subquery values meet the condition
--is used with SELECT, WHERE and HAVING statements, ALL means that the condition will be true only if the operation is true for all values in the range. 
SELECT ALL firstname, lastname
FROM students
WHERE TRUE;

SELECT firstname
FROM students 
WHERE courseid = ALL (
    SELECT courseid 
    FROM courses 
    WHERE credits = 55
);

--The SELECT INTO statement copies data from one table into a new table.
SELECT * INTO CustomersBackup2024
FROM students;

select * from CustomersBackup2024;

--Another example of select INTO
SELECT s.studentid, s.firstname, s.lastname, c.CourseName
INTO EnrolledStudents
FROM students s
JOIN courses c ON s.courseid = c.courseid;

select * from enrolledstudents e ;

--SQL INSERT INTO SELECT Statement
--The INSERT INTO SELECT statement copies data from one table and inserts it into another table.
--The INSERT INTO SELECT statement requires that the data types in source and target tables match.
INSERT INTO customersbackup2024(studentid, firstname , lastname)
SELECT studentid , firstname , lastname FROM enrolledstudents 
WHERE coursename ='BCA';

select * from customersbackup2024 c2 ;


--SQL CASE

select * from payment c2 ;
SELECT firstname, courseid,
CASE
    WHEN courseid < 104 THEN 'This is undergraduate course'
    ELSE 'This is postgraduate course'
END AS CourseDescription
FROM students;

--NULL functions
--IF NULL()This function returns a specified value if the expression is NULL; otherwise, it returns the expression itself.
/*
select firstname, ifnull(courseid , -1) as courseid 
FROM students;
*/
--Only COALESCE function work in postgresql
SELECT studentid , firstname, COALESCE(courseid , NULL) AS courseid 
FROM students;


--SQL Stored Procedures for SQL Server
--A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.
--stored procedure example for for SQL ********Not working in postgresql 
/*
create procedure selectallstudents
as 
select * from students;
go;

*/

/*
CREATE PROCEDURE SelectAllStudents
AS
BEGIN
    SELECT * FROM Students;
END;
go
*/

--Postgresql stored procedure example
create or replace function selectallstudents()
returns table(studentid int, email varchar, firstname varchar, lastname varchar, courseid int) as 
$$
begin 
	return query select s.studentid, s.email, s.firstname, s.lastname, s.courseid from students as s;
end;
$$ language plpgsql;


select * from selectallstudents();


create or replace function insertstudents(
studentid int, email varchar, firstname varchar, lastname varchar, courseid int
)
$$
begin 
	insert into students(studentid, email, firstname, lastname, courseid)
    values (s.studentid, s.email, s.firstname, s.lastname, s.courseid) as s;
end;
$$ language plpgsql;


select * from Students;


CREATE OR REPLACE PROCEDURE InsertStudents(
    p_student_id INT,
    p_email VARCHAR,
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_courseid INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Students(studentid, email, firstname, lastname, courseid)
    VALUES (p_student_id, p_email, p_first_name, p_last_name, p_courseid);
END;
$$;

CALL InsertStudents(19,'jinendra@gmail.com','Jinendra','Kumar',201);

CALL InsertStudent(
    17,                             -- p_student_id as INT
    'jitendra@gmail.com'::VARCHAR,      -- p_email as VARCHAR
    'JItendra'::VARCHAR,           -- p_first_name as VARCHAR   
    'Kumar'::VARCHAR,               -- p_last_name as VARCHAR      
    201                             -- p_age as INT
);


CREATE OR REPLACE PROCEDURE InsertStudents(
    p_student_id INT,
    p_email VARCHAR,
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_courseid INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Students(studentid, email, firstname, lastname, courseid)
    VALUES (p_student_id, p_email, p_first_name, p_last_name, p_courseid);
END;
$$;


DROP FUNCTION IF EXISTS selectallstudents();
DROP PROCEDURE IF EXISTS InsertStudent();



select * from students s ;


-- single comment
/* Multipline comment 
 * example
 * */

--SQL Operators
--1. Arithmetic Operators
SELECT 5 + 3; --results in 8
SELECT 10 - 4; --results in 6
SELECT 7 * 2; --results in 14
SELECT 8 / 2; --results in 4
SELECT 10 % 3; --results in 1

--2. Comparison Operators
SELECT * FROM Students WHERE studentid = 2;
SELECT * FROM Students WHERE studentid != 2;
SELECT * FROM Students WHERE studentid > 2;
SELECT * FROM Students WHERE studentid < 2;
SELECT * FROM Students WHERE studentid >= 8;
SELECT * FROM Students WHERE studentid <= 3;

--3. Logical Operators
--These operators are used to combine multiple conditions.


SELECT * FROM Students WHERE studentid > 12 AND courseid = '201';

SELECT * FROM Students WHERE studentid > 18 OR courseid = '201';

--*************************************Need to revise*****************
SELECT * FROM Students WHERE NOT (courseid < 201);


--4. Bitwise Operators
--These operators perform operations on binary representations.

--5. String Operators
SELECT * FROM Students WHERE firstname LIKE 'J%'; --(names starting with 'J') pattern matching

SELECT * FROM Students WHERE firstname  ILIKE 'j%'; --Case-insensitive pattern matching	

--6. NULL Operators -These operators are used to test for NULL values.
SELECT * FROM Students WHERE courseid IS NULL;
SELECT * FROM Students WHERE courseid IS NOT NULL;

--7 IN Operator -Checks if a value exists within a set of values.
SELECT * FROM Students WHERE courseid IN (101, 102, 103);

--8. BETWEEN Operator -Checks if a value is within a range.
SELECT * FROM Students WHERE courseid BETWEEN 101 AND 102;






--SQL INDEX - Indexing creates a separate memory location and stored column in a sorted manner and also save pointer for memory location
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











