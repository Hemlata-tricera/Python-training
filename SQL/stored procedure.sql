/*A stored procedure in SQL is a group of SQL queries that can be saved and reused multiple times. 
It is very useful as it reduces the need for rewriting SQL queries. 
It enhances efficiency, reusability, and security in database management.


Syntax for Creating a Stored Procedure
In PostgreSQL, the basic syntax for creating a stored procedure is:

CREATE OR REPLACE PROCEDURE procedure_name(parameter1 data_type, parameter2 data_type, ...)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Procedure logic goes here
END;
$$;


Step-1:
Let's create a simple stored procedure that inserts a new student into the Students table.
*/


CREATE OR REPLACE PROCEDURE InsertStudent(
    p_student_id INT,
    p_email VARCHAR,
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_courseid INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO students(studentid, email, firstname, lastname, courseid)
    VALUES (p_student_id, p_email, p_first_name, p_last_name, p_courseid);
END;
$$;


-- Step 2: Calling the Stored Procedure, You can call the stored procedure using the CALL statement:
CALL InsertStudent(20,'harish@gmail.com','Harish','Kumar',201);


--Step 3: Querying the Table
select * from students;


/* Let's create a stored procedure to update student records in the Students table. 
 This procedure will allow you to update a student's information.
 
 Step 1: Create the Stored Procedure
*/

CREATE OR REPLACE PROCEDURE update_student(
    p_student_id INT,
    p_email VARCHAR,
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_courseid INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Students
    SET firstname = p_first_name,
        lastname = p_last_name,
        email = p_email,
        courseid = p_courseid
    WHERE studentid = p_student_id;

    IF NOT FOUND THEN
        RAISE NOTICE 'No student found with ID %', p_student_id;
    ELSE
        RAISE NOTICE 'Student with ID % updated successfully.', p_student_id;
    END IF;
END;
$$;


--Step 3: Calling the Stored Procedure

CALL update_student(1, 'john.newemail@example.com', 'John', 'Doe', 201);

--Step 4: Querying the Table -After executing the update, you can verify the changes with:
select * from students;


--Delete record - This procedure will encapsulate the logic for safely deleting a record.
-- Step 1: Create the Stored Procedure


CREATE OR REPLACE PROCEDURE delete_student(
    p_student_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Students
    WHERE studentid = p_student_id;

    IF NOT FOUND THEN
        RAISE NOTICE 'No student found with ID %', p_student_id;
    ELSE
        RAISE NOTICE 'Student with ID % deleted successfully.', p_student_id;
    END IF;
END;
$$;

--Step 3: Calling the Stored Procedure
CALL delete_student(6);

--Step 4: Querying the Table- After calling the procedure, you can check the Students table to verify the deletion:
select * from students;



