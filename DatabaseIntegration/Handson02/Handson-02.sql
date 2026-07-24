USE college_db;

INSERT INTO departments (dept_name, head_of_dept, budget) VALUES
('Computer Science','Dr. Ravi Kumar',500000),
('Electronics','Dr. Priya Sharma',400000),
('Mechanical','Dr. Arun Kumar',350000);

INSERT INTO students
(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Prasanna','I','prasanna@gmail.com','2003-05-10',1,2022),
('Anita','Reddy','anita@gmail.com','2002-11-20',1,2021),
('Kiran','Kumar','kiran@gmail.com','2003-01-15',2,2022),
('Sneha','Patel','sneha@gmail.com','2002-09-18',3,2021),
('Vijay','Singh','vijay@gmail.com','2003-03-22',2,2023);

INSERT INTO courses
(course_name,course_code,credits,department_id,max_seats)
VALUES
('Database Systems','CS101',4,1,60),
('Data Structures','CS102',4,1,60),
('Digital Electronics','EC201',3,2,50),
('Thermodynamics','ME301',4,3,40);

INSERT INTO professors
(prof_name,email,department_id,salary)
VALUES
('Dr. Ramesh','ramesh@college.com',1,90000),
('Dr. Suresh','suresh@college.com',2,85000),
('Dr. Meena','meena@college.com',3,80000);

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(1,1,'2024-01-10','A'),
(2,2,'2024-01-10','B'),
(3,3,'2024-01-11','A'),
(4,4,'2024-01-12','C'),
(5,3,'2024-01-13','B');

SELECT * FROM departments;
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM professors;
SELECT * FROM enrollments;

UPDATE students
SET enrollment_year = 2024
WHERE student_id = 1;

UPDATE professors
SET salary = salary + 5000
WHERE department_id = 1;

DELETE FROM enrollments
WHERE enrollment_id = 5;

SELECT * FROM students;
SELECT * FROM professors;
SELECT * FROM enrollments;