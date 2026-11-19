Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:

psql (18.7)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=# CREATE DATABASE college0;
CREATE DATABASE
postgres=# \c college0
You are now connected to database "college0" as user "postgres".
college0=# \l
                                                                    List of databases
   Name    |  Owner   | Encoding | Locale Provider |          Collate           |           Ctype            | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+----------------------------+----------------------------+--------+-----------+-----------------------
 ArunDB    | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 collage   | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 college   | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 college0  | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 college1  | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 college2  | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 postgres  | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           | =c/postgres          +
           |          |          |                 |                            |                            |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_United States.1252 | English_United States.1252 |        |           | =c/postgres          +
           |          |          |                 |                            |                            |        |           | postgres=CTc/postgres
(9 rows)


college0=# CREATE TABLE students (
college0(#     student_id SERIAL PRIMARY KEY,
college0(#     name VARCHAR(50),
college0(#     age INT,
college0(#     department VARCHAR(50),
college0(#     marks INT
college0(# );
CREATE TABLE
college0=# INSERT INTO students (name, age, department, marks)
college0-# VALUES
college0-# ('Rahul', 20, 'CSE', 85),
college0-# ('Priya', 21, 'ECE', 90),
college0-# ('Amit', 19, 'MECH', 78);
INSERT 0 3
college0=# SELECT * FROM students;
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          1 | Rahul |  20 | CSE        |    85
          2 | Priya |  21 | ECE        |    90
          3 | Amit  |  19 | MECH       |    78
(3 rows)


college0=# INSERT INTO students (name, age, department, marks)
college0-# VALUES
college0-# ('Rahul', 20, 'CSE', 85),
college0-# ('Priya', 21, 'ECE', 90),
college0-# ('Amit', 19, 'MECH', 78),
college0-# ('Sneha', 20, 'CSE', 95),
college0-# ('Kiran', 22, 'ECE', 70);
INSERT 0 5
college0=# SELECT * FROM students;
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          1 | Rahul |  20 | CSE        |    85
          2 | Priya |  21 | ECE        |    90
          3 | Amit  |  19 | MECH       |    78
          4 | Rahul |  20 | CSE        |    85
          5 | Priya |  21 | ECE        |    90
          6 | Amit  |  19 | MECH       |    78
          7 | Sneha |  20 | CSE        |    95
          8 | Kiran |  22 | ECE        |    70
(8 rows)


college0=# UPDATE students
college0-# SET marks = 95
college0-# WHERE id = 1;
ERROR:  column "id" does not exist
LINE 3: WHERE id = 1;
              ^
college0=# DELETE FROM students
college0-# WHERE id = 2;
ERROR:  column "id" does not exist
LINE 2: WHERE id = 2;
              ^
college0=# SELECT * FROM students
college0-# ORDER BY marks ASC;
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          8 | Kiran |  22 | ECE        |    70
          6 | Amit  |  19 | MECH       |    78
          3 | Amit  |  19 | MECH       |    78
          1 | Rahul |  20 | CSE        |    85
          4 | Rahul |  20 | CSE        |    85
          5 | Priya |  21 | ECE        |    90
          2 | Priya |  21 | ECE        |    90
          7 | Sneha |  20 | CSE        |    95
(8 rows)


college0=# SELECT * FROM students
college0-# ORDER BY marks DESC;
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          7 | Sneha |  20 | CSE        |    95
          2 | Priya |  21 | ECE        |    90
          5 | Priya |  21 | ECE        |    90
          1 | Rahul |  20 | CSE        |    85
          4 | Rahul |  20 | CSE        |    85
          6 | Amit  |  19 | MECH       |    78
          3 | Amit  |  19 | MECH       |    78
          8 | Kiran |  22 | ECE        |    70
(8 rows)


college0=# SELECT * FROM students
college0-# WHERE marks > 80;
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          1 | Rahul |  20 | CSE        |    85
          2 | Priya |  21 | ECE        |    90
          4 | Rahul |  20 | CSE        |    85
          5 | Priya |  21 | ECE        |    90
          7 | Sneha |  20 | CSE        |    95
(5 rows)


college0=# SELECT * FROM students
college0-# WHERE age > 19 AND marks > 80;
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          1 | Rahul |  20 | CSE        |    85
          2 | Priya |  21 | ECE        |    90
          4 | Rahul |  20 | CSE        |    85
          5 | Priya |  21 | ECE        |    90
          7 | Sneha |  20 | CSE        |    95
(5 rows)


college0=# SELECT * FROM students
college0-# WHERE department = 'CSE' OR department = 'ECE';
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          1 | Rahul |  20 | CSE        |    85
          2 | Priya |  21 | ECE        |    90
          4 | Rahul |  20 | CSE        |    85
          5 | Priya |  21 | ECE        |    90
          7 | Sneha |  20 | CSE        |    95
          8 | Kiran |  22 | ECE        |    70
(6 rows)


college0=# SELECT * FROM students
college0-# WHERE NOT department = 'CSE';
 student_id | name  | age | department | marks
------------+-------+-----+------------+-------
          2 | Priya |  21 | ECE        |    90
          3 | Amit  |  19 | MECH       |    78
          5 | Priya |  21 | ECE        |    90
          6 | Amit  |  19 | MECH       |    78
          8 | Kiran |  22 | ECE        |    70
(5 rows)


college0=# ALTER TABLE students
college0-# ADD email VARCHAR(100);
ALTER TABLE
college0=# SELECT DISTINCT department
college0-# FROM students;
 department
------------
 CSE
 MECH
 ECE
(3 rows)


college0=# SELECT * FROM students
college0-# WHERE name LIKE 'A%';
 student_id | name | age | department | marks | email
------------+------+-----+------------+-------+-------
          3 | Amit |  19 | MECH       |    78 |
          6 | Amit |  19 | MECH       |    78 |
(2 rows)


college0=# SELECT * FROM students
college0-# WHERE marks BETWEEN 70 AND 90;
 student_id | name  | age | department | marks | email
------------+-------+-----+------------+-------+-------
          1 | Rahul |  20 | CSE        |    85 |
          2 | Priya |  21 | ECE        |    90 |
          3 | Amit  |  19 | MECH       |    78 |
          4 | Rahul |  20 | CSE        |    85 |
          5 | Priya |  21 | ECE        |    90 |
          6 | Amit  |  19 | MECH       |    78 |
          8 | Kiran |  22 | ECE        |    70 |
(7 rows)


college0=# SELECT * FROM students
college0-# WHERE department IN ('CSE', 'ECE');
 student_id | name  | age | department | marks | email
------------+-------+-----+------------+-------+-------
          1 | Rahul |  20 | CSE        |    85 |
          2 | Priya |  21 | ECE        |    90 |
          4 | Rahul |  20 | CSE        |    85 |
          5 | Priya |  21 | ECE        |    90 |
          7 | Sneha |  20 | CSE        |    95 |
          8 | Kiran |  22 | ECE        |    70 |
(6 rows)


college0=# SELECT department, COUNT(*)
college0-# FROM students
college0-# GROUP BY department;
 department | count
------------+-------
 CSE        |     3
 MECH       |     2
 ECE        |     3
(3 rows)


college0=# SELECT department, AVG(marks)
college0-# FROM students
college0-# GROUP BY department
college0-# HAVING AVG(marks) > 80;
 department |         avg
------------+---------------------
 CSE        | 88.3333333333333333
 ECE        | 83.3333333333333333
(2 rows)


college0=# CREATE TABLE student (
college0(#     student_id INT PRIMARY KEY,
college0(#     name VARCHAR(50)
college0(# );
CREATE TABLE
college0=#
college0=# CREATE TABLE id_card (
college0(#     card_id INT PRIMARY KEY,
college0(#     student_id INT UNIQUE REFERENCES student(student_id),
college0(#     issue_date DATE
college0(# );
CREATE TABLE
college0=# CREATE TABLE department (
college0(#     dept_id INT PRIMARY KEY,
college0(#     dept_name VARCHAR(50)
college0(# );
CREATE TABLE
college0=#
college0=# CREATE TABLE students (
college0(#     student_id INT PRIMARY KEY,
college0(#     name VARCHAR(50),
college0(#     dept_id INT REFERENCES department(dept_id)
college0(# );
ERROR:  relation "students" already exists
college0=# CREATE TABLE department (
college0(#     dept_id INT PRIMARY KEY,
college0(#     dept_name VARCHAR(50)
college0(# );
ERROR:  relation "department" already exists
college0=#
college0=# CREATE TABLE students (
college0(#     student_id INT PRIMARY KEY,
college0(#     name VARCHAR(50),
college0(#     dept_id INT REFERENCES department(dept_id)
college0(# );
ERROR:  relation "students" already exists
college0=# insert into student_card(card_number,id)
college0-# values
college0-# ('card101'1),
college0-# ('card102',2);
ERROR:  syntax error at or near "1"
LINE 3: ('card101'1),
                  ^
college0=# ('card101',1),
college0-# ('card102',2);
ERROR:  syntax error at or near "'card101'"
LINE 1: ('card101',1),
         ^
college0=# INSERT INTO id_card (card_id, student_id)
college0-# VALUES
college0-# (101, 1),
college0-# (102, 2);
ERROR:  insert or update on table "id_card" violates foreign key constraint "id_card_student_id_fkey"
DETAIL:  Key (student_id)=(1) is not present in table "student".
college0=# ALTER TABLE id_card
college0-# ALTER COLUMN card_id TYPE VARCHAR(20);
ALTER TABLE
college0=# INSERT INTO id_card (card_id, student_id)
college0-# VALUES
college0-# ('card101', 1),
college0-# ('card102', 2);
ERROR:  insert or update on table "id_card" violates foreign key constraint "id_card_student_id_fkey"
DETAIL:  Key (student_id)=(1) is not present in table "student".
college0=# SELECT * FROM id_card;
 card_id | student_id | issue_date
---------+------------+------------
(0 rows)


college0=# CREATE TABLE Departments (
college0(#     DepartmentID INT PRIMARY KEY,
college0(#     DepartmentName VARCHAR(100) NOT NULL,
college0(#     HODName VARCHAR(100),
college0(#     NumberOfEmployees INT DEFAULT 0,
college0(#     Status VARCHAR(20) DEFAULT 'Active'
college0(# );
CREATE TABLE
college0=# INSERT INTO Departments
college0-# (DepartmentID, DepartmentName, HODName, NumberOfEmployees, Status)
college0-# VALUES
college0-# (1, 'Human Resources', 'Rahul', 10, 'Active'),
college0-# (2, 'Finance', 'Priya', 8, 'Active'),
college0-# (3, 'Information Technology', 'Arun', 15, 'Active'),
college0-# (4, 'Marketing', 'Sneha', 12, 'Active'),
college0-# (5, 'Sales', 'Amit', 20, 'Active'),
college0-# (6, 'Operations', 'Kiran', 18, 'Active'),
college0-# (7, 'Administration', 'Anjali', 5, 'Active'),
college0-# (8, 'Customer Support', 'Vijay', 14, 'Active');
INSERT 0 8
college0=# SELECT * FROM Departments;
 departmentid |     departmentname     | hodname | numberofemployees | status
--------------+------------------------+---------+-------------------+--------
            1 | Human Resources        | Rahul   |                10 | Active
            2 | Finance                | Priya   |                 8 | Active
            3 | Information Technology | Arun    |                15 | Active
            4 | Marketing              | Sneha   |                12 | Active
            5 | Sales                  | Amit    |                20 | Active
            6 | Operations             | Kiran   |                18 | Active
            7 | Administration         | Anjali  |                 5 | Active
            8 | Customer Support       | Vijay   |                14 | Active
(8 rows)


college0=# CREATE TABLE Employees (
college0(#     EmployeeID INT PRIMARY KEY,
college0(#     FirstName VARCHAR(50) NOT NULL,
college0(#     LastName VARCHAR(50),
college0(#     Gender VARCHAR(10),
college0(#     Email VARCHAR(100) UNIQUE,
college0(#     Phone VARCHAR(15),
college0(#     DateOfBirth DATE,
college0(#     HireDate DATE,
college0(#     Salary DECIMAL(10,2),
college0(#     DepartmentID INT,
college0(#     Designation VARCHAR(100),
college0(#     Status VARCHAR(20) DEFAULT 'Active',
college0(#
college0(#     FOREIGN KEY (DepartmentID)
college0(#     REFERENCES Departments(DepartmentID)
college0(# );
CREATE TABLE
college0=# INSERT INTO Employees
college0-# (EmployeeID, FirstName, LastName, Gender, Email,
college0(# Phone, DateOfBirth, HireDate, Salary, DepartmentID,
college0(# Designation, Status)
college0-# VALUES
college0-# (101, 'Rahul', 'Sharma', 'Male', 'rahul@gmail.com',
college0(# '9876543210', '1998-05-12', '2022-01-10', 35000, 3,
college0(# 'Software Developer', 'Active'),
college0-#
college0-# (102, 'Priya', 'Kumar', 'Female', 'priya@gmail.com',
college0(# '9876543211', '1997-08-15', '2021-03-15', 45000, 1,
college0(# 'HR Executive', 'Active'),
college0-#
college0-# (103, 'Arun', 'Kumar', 'Male', 'arun@gmail.com',
college0(# '9876543212', '1995-02-20', '2020-06-01', 55000, 3,
college0(# 'Team Leader', 'Active'),
college0-#
college0-# (104, 'Sneha', 'Reddy', 'Female', 'sneha@gmail.com',
college0(# '9876543213', '1999-11-25', '2023-02-10', 30000, 4,
college0(# 'Marketing Executive', 'Active'),
college0-#
college0-# (105, 'Amit', 'Verma', 'Male', 'amit@gmail.com',
college0(# '9876543214', '1996-04-18', '2022-08-05', 40000, 5,
college0(# 'Sales Executive', 'Active');
INSERT 0 5
college0=# SELECT * FROM Employees;
 employeeid | firstname | lastname | gender |      email      |   phone    | dateofbirth |  hiredate  |  salary  | departmentid |     designation     | status
------------+-----------+----------+--------+-----------------+------------+-------------+------------+----------+--------------+---------------------+--------
        101 | Rahul     | Sharma   | Male   | rahul@gmail.com | 9876543210 | 1998-05-12  | 2022-01-10 | 35000.00 |            3 | Software Developer  | Active
        102 | Priya     | Kumar    | Female | priya@gmail.com | 9876543211 | 1997-08-15  | 2021-03-15 | 45000.00 |            1 | HR Executive        | Active
        103 | Arun      | Kumar    | Male   | arun@gmail.com  | 9876543212 | 1995-02-20  | 2020-06-01 | 55000.00 |            3 | Team Leader         | Active
        104 | Sneha     | Reddy    | Female | sneha@gmail.com | 9876543213 | 1999-11-25  | 2023-02-10 | 30000.00 |            4 | Marketing Executive | Active
        105 | Amit      | Verma    | Male   | amit@gmail.com  | 9876543214 | 1996-04-18  | 2022-08-05 | 40000.00 |            5 | Sales Executive     | Active
(5 rows)


college0=# SELECT
college0-#     E.EmployeeID,
college0-#     E.FirstName,
college0-#     E.LastName,
college0-#     E.Salary,
college0-#     E.Designation,
college0-#     D.DepartmentName
college0-# FROM Employees E
college0-# INNER JOIN Departments D
college0-# ON E.DepartmentID = D.DepartmentID;
 employeeid | firstname | lastname |  salary  |     designation     |     departmentname
------------+-----------+----------+----------+---------------------+------------------------
        101 | Rahul     | Sharma   | 35000.00 | Software Developer  | Information Technology
        102 | Priya     | Kumar    | 45000.00 | HR Executive        | Human Resources
        103 | Arun      | Kumar    | 55000.00 | Team Leader         | Information Technology
        104 | Sneha     | Reddy    | 30000.00 | Marketing Executive | Marketing
        105 | Amit      | Verma    | 40000.00 | Sales Executive     | Sales
(5 rows)


college0=# SELECT *
college0-# FROM Employees
college0-# WHERE DepartmentID = 3;
 employeeid | firstname | lastname | gender |      email      |   phone    | dateofbirth |  hiredate  |  salary  | departmentid |    designation     | status
------------+-----------+----------+--------+-----------------+------------+-------------+------------+----------+--------------+--------------------+--------
        101 | Rahul     | Sharma   | Male   | rahul@gmail.com | 9876543210 | 1998-05-12  | 2022-01-10 | 35000.00 |            3 | Software Developer | Active
        103 | Arun      | Kumar    | Male   | arun@gmail.com  | 9876543212 | 1995-02-20  | 2020-06-01 | 55000.00 |            3 | Team Leader        | Active
(2 rows)


college0=# SELECT *
college0-# FROM Employees
college0-# WHERE Salary > 30000;
 employeeid | firstname | lastname | gender |      email      |   phone    | dateofbirth |  hiredate  |  salary  | departmentid |    designation     | status
------------+-----------+----------+--------+-----------------+------------+-------------+------------+----------+--------------+--------------------+--------
        101 | Rahul     | Sharma   | Male   | rahul@gmail.com | 9876543210 | 1998-05-12  | 2022-01-10 | 35000.00 |            3 | Software Developer | Active
        102 | Priya     | Kumar    | Female | priya@gmail.com | 9876543211 | 1997-08-15  | 2021-03-15 | 45000.00 |            1 | HR Executive       | Active
        103 | Arun      | Kumar    | Male   | arun@gmail.com  | 9876543212 | 1995-02-20  | 2020-06-01 | 55000.00 |            3 | Team Leader        | Active
        105 | Amit      | Verma    | Male   | amit@gmail.com  | 9876543214 | 1996-04-18  | 2022-08-05 | 40000.00 |            5 | Sales Executive    | Active
(4 rows)


college0=#