/*Create a SQL database called "Bookstore" with a table named "Books" containing columns for book ID, title, author, genre, and price. Insert at least five sample records into the table. Write SQL queries to retrieve all data from the "Books" table.*/


create table Books(
	BookID SERIAL not null,   -- Auto-incrementing primary key using SERIAL
	Title VARCHAR(255) not null,
	Author VARCHAR(255) not null,
 	Genre VARCHAR(100),
 	Price DECIMAL(10, 2) not null,
 	constraint pk_books primary key (BookID),
 	constraint chk_price check (price > 0),
 	constraint uq_title_author unique (Title, Author)  -- Ensures Title-Author combination is unique
);


insert into Books(Title, Author, Genre, Price)
values 
('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 10.99),
('1984', 'George Orwell', 'Dystopian', 8.99),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 7.99),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 6.99),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 12.99);


select * from Books;



/* The bookstore manager wants to view books of a specific genre and sort them by price. 
 * Assignment-Write SQL queries to filter books by genre (e.g., "Mystery") and sort them by price in ascending order. Experiment with different genres and observe the results. 
 */





