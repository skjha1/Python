Show databases;

use Student;

Show tables;

Select * from students;

drop database Student;

create database Student_Info;
create database CompanyDB;
use CompanyDB;

create table Employees ( 
	EmployeeID INT auto_increment primary key,
    FirstName varchar(50) Not null,
    LastName varchar(50) Not null,
    DateOfBirth Date not null,
    Email varchar(100) unique not null,
    HireDate Date not null,
    DepartmentID Int
    );
    
    Select * from Employees;
    
    insert into Employees (FirstName, LastName, DateOfBirth, Email, HireDate, DepartmentID)
    values
    ('Sushma', 'Mishra', '2000-04-23', 'sushma@gmail.com', '2022-08-15', 1),
     ('Swati', 'Chaudhary', '2004-04-23', 'swati@gmail.com', '2023-08-15', 1),
     ('Suman', 'Kumar', '2002-04-23', 'Suman@gmail.com', '2020-08-15', 1);
     
      insert into Employees (FirstName, LastName, DateOfBirth, Email, HireDate, DepartmentID)
    values
    ('Astha', 'Mishra', '2000-04-23', 'astha@gmail.com', '2022-08-15', 2),
     ('Ram', 'Chaudhary', '2004-04-23', 'ram@gmail.com', '2023-08-15', 3),
     ('Shayam', 'Kumar', '2002-04-23', 'shyam@gmail.com', '2020-08-15', 4);
	
     
         Select * from Employees;
     
Select HireDate from Employees where FirstName = 'Swati';



    
create table Department ( 
	DepartmentID INT auto_increment primary key,
    DepartmentName varchar(100) not null
    );
    
    Select * from Department;
    
       insert into Department (DepartmentName)
    values
	('Human Resources'),
    ('Engineering'),
    ('Sales'),
    ('Marketing');

Select d.DepartmentName, concat(e.FirstName, ' ', e.LastName) AS EmployeeName
from 
	Employees e
join 
	Department d
On 
	e.DepartmentID = d.DepartmentID;

	




