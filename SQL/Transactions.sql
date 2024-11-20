/* PostgreSQL – Transactions
A PostgreSQL transaction is a sequence of one or more SQL operations that are executed as a single unit. Transactions ensure that all operations within them are completed successfully (committed) or none at all (rolled back), maintaining data integrity and consistency.

Key Properties of Transactions (ACID):
Atomicity: All operations in a transaction are treated as a single unit. If one fails, the entire transaction fails.
Consistency: A transaction takes the database from one valid state to another, ensuring all rules are followed.
Isolation: Transactions operate independently, so the intermediate state of a transaction is not visible to others.
Durability: Once a transaction is committed, its changes are permanent, even in the event of a failure.

Basic Commands:
BEGIN: Start a transaction.
COMMIT: Save all changes made in the transaction.
ROLLBACK: Undo all changes if something goes wrong.


*/
--Here we have student table
select * from student; ;

--Example- inserting a student and updating another student’s
BEGIN;

-- Attempt to add a new student
INSERT INTO students (studentid, firstname, courseid) VALUES (23, 'Eve', 101);

-- Attempt to update a student's GPA
UPDATE students SET courseid = 202 WHERE firstname = 'John';

-- If successful, commit
COMMIT;  -- or ROLLBACK if there's an error