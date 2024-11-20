create table employee(
id int,
name varchar);

insert into employee values(1, 'Jayesh');

select * from employee;

insert into employee (id, name)
values
(2, 'Ramesh'),
(3, 'Suresh'),
(4, 'Rakesh');

select * from employee;

create table cars(
brand VARCHAR(255),
model VARCHAR(255),
year INT
);

select * from cars;

insert into cars(brand, model, year)
values
('Ford', 'Mustang', 1964),
('Volvo', 'p1800', 1968),
('BMW', 'M1', 1978),
('Toyto', 'Celia', 1975);

select * from cars;

select brand, year from cars;

insert into cars (brand, model, year)
values
('Ford', 'Mustang', 1964),
('Toyto', 'Celia', 1975);

select * from cars;

select distinct brand from cars;

select * from cars
where brand='Toyto';

select * from cars 
where year=1964;

select * from cars 
where year > 1964;

select * from cars 
where year between 1964 and 1975;

select * from cars
where model ilike 'C%';  --ilike keyword in postgres

select * from cars 
where model in ('M1', 'Celia');

select * from cars 
where year <> 1975;

insert into cars
values
('DFord', 'DMustang', 1964),
('DVolvo', 'Dp1800', 1968),
('DBMW', 'DM1', 1978),
('DToyto', 'DCelia', 1975);

insert into cars
values
('DFord', 'CMustang', 1964),
('DVolvo', 'cp1800', 1968);

select * from cars;


--The ORDER BY keyword is used to sort the result-set in ascending or descending order.
select * from cars
order by year;

select * from cars 
order by year desc; --To sort the records in descending order, use the DESC keyword.

select * from cars 
order by brand -- will order alphabetically

select  * from cars 
order by model 

select * from cars 
order by model desc 

select * from cars 
order by brand desc 

select * from cars 
order by brand, model 

create table customer(
cust_id int,
dept_id int,
first_name varchar(250),
last_name varchar(250),
email varchar(250)
);

insert into customer 
values
(101, 1, 'Jayesh', 'Pawar', 'jayesh@gmail.com'),
(102, 2, 'Rayesh', 'Pawar', 'rayesh@gmail.com'),
(103, 2, 'Suyash', 'Patil', 'suyash@gmail.com'),
(104, 1, 'Jay', 'Pawar', 'jay@gmail.com'),
(105, 2, 'Swati', 'Chajed', 'swati@gmail.com'),
(106, 1, 'Minal', 'Dhar', 'minal@gmail.com'),
(107, 1, 'Radha', 'Goswami', 'radha@gmail.com'),
(108, 1, 'Dhiru', 'Ambani', 'dhiru@gmail.com'),
(109, 2, 'Swasti', 'Mehul', 'swasti@gmail.com'),
(110, 1, 'Radha', 'Rani', 'radhaa@gmail.com');



select * from customer;

select * from customer
where last_name = 'Pawar' and dept_id =1;

select * from customer 
where dept_id = 2 and (first_name like 'R%' or first_name like 'S%');







