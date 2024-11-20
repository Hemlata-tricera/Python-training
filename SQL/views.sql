/* VIEW is a virtual table that is based on the result of a SELECT query. Views can simplify complex queries, 
 enhance security by restricting access to specific columns or rows, 
 and provide a way to present data in a specific format without storing the data separately.
 
 Syntax for Creating a View

 
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

Example of Creating and Using Views
Step 1: Create the Base Table
We have students table, for checking students table use below query
*/

select * from students;

--Step 2: Create a View
--Now, let’s create a view to show only the students enrolled in "BCA"(that is 101 courseid).

CREATE VIEW BCAStudents AS
SELECT studentid, firstname, lastname, email
FROM students
WHERE courseid = 101;

--Step 3: Query the View
--You can query the view just like you would a regular table:
SELECT * FROM BCAStudents;

/* The output of the above query would be:

4	Jayesh	Shirsath	jayesh@gmail.com
21	Vijaya	Marathe	vijaya@gmail.com

*/

--Step 4: Updating the View
--If you update the underlying table, the view will reflect those changes. For instance, if we update Jayesh course:
UPDATE students
SET courseid = 103
WHERE studentid = 4;

--Step 5 Now, querying the view again will give result, as there are only 1 students in "BCA":
SELECT * FROM BCAStudents;
--O/P  21	Vijaya	Marathe	vijaya@gmail.com

--Step 6: Dropping the View
--If you need to remove the view, you can use:
DROP VIEW BCAStudents;







