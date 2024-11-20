/* Triggers are stored programs or procedures, Which are automatically executed or fired when some events occur. 
Events can be any of the following-

1. Database Manipulation(DML): statement like - DELETE, INSERT ot UPDATE
2. Database defination(DDL): statement like - CREATE, ALTER or DROP
3. Database Operation: like LOGON, LOGOFF, STATUP or SHUTDOWN

Triggers can be defined on the table, view, schema or database with which the event is associated

Syntax-
create trigger [trigger_name] 


[before | after]  


{insert | update | delete}  


on [table_name]  


[for each row | for each statement]  


[trigger_body] 

Explanation of Syntax
Create trigger [trigger_name]: Creates or replaces an existing trigger with the trigger_name.
[before | after]: This specifies when the trigger will be executed.
{insert | update | delete}: This specifies the DML operation.
On [table_name]: This specifies the name of the table associated with the trigger.
[for each row]: This specifies a row-level trigger, i.e., the trigger will be executed for each affected row.
[trigger_body]: This provides the operation to be performed as the trigger is fired


Step 1: Create the Necessary Tables
We have already created student table
*/
select * from students;

-- When the name of an student changes, we log the changes in a separate table named ‘STUD_ENROLL’:

CREATE TABLE STUD_ENROLL(
   STD_ID INT NOT NULL,
   ENTRY_DATE TEXT NOT NULL
);

--Step 2: Define the Trigger function
--First, define a new function called studlog():

CREATE OR REPLACE FUNCTION studlog() RETURNS TRIGGER AS $$
BEGIN
   INSERT INTO STUD_ENROLL(STD_ID, ENTRY_DATE) VALUES (NEW.studentid, current_timestamp);
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

--Step 3: Create and Bind the Trigger
--We create a trigger named ‘example_trigger' that fires after an ‘INSERT' event on the ‘STUDENTS' table:
CREATE TRIGGER example_trigger 
AFTER INSERT ON students
FOR EACH ROW 
EXECUTE FUNCTION studlog();

--Step 4: Insert Sample Data and Verify
--Insert some sample data for testing. We insert a row into the student table.
insert into students values(22, 'vijay@gmail.com', 'Vijay', 'Marathe', 102);

--Step-5 :To examine the student table use the below query:
select * from students;


--Step-6 :To examine the stud_enrollment table use the below query:

select * from STUD_ENROLL;
