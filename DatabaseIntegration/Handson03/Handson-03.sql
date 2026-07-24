USE college_db;

-- VIEW

CREATE OR REPLACE VIEW student_details AS
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;

SELECT * FROM student_details;

-- INNER JOIN

SELECT
    s.first_name,
    c.course_name,
    e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;

-- LEFT JOIN

SELECT
    s.first_name,
    c.course_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
LEFT JOIN courses c
ON e.course_id = c.course_id;

-- GROUP BY

SELECT
    department_id,
    COUNT(*) AS total_students
FROM students
GROUP BY department_id;

-- HAVING

SELECT
    department_id,
    COUNT(*) AS total_students
FROM students
GROUP BY department_id
HAVING COUNT(*) >= 1;

-- ORDER BY

SELECT *
FROM students
ORDER BY first_name;

-- INDEX

CREATE INDEX idx_student_email
ON students(email);

SHOW INDEX FROM students;

-- TRANSACTION

START TRANSACTION;

UPDATE professors
SET salary = salary + 1000
WHERE professor_id = 1;

SAVEPOINT sp1;

UPDATE professors
SET salary = salary + 1000
WHERE professor_id = 2;

ROLLBACK TO sp1;

COMMIT;

-- STORED PROCEDURE

DELIMITER $$

CREATE PROCEDURE GetStudents()
BEGIN
    SELECT * FROM students;
END $$

DELIMITER ;

CALL GetStudents();

-- FUNCTION

DELIMITER $$

CREATE FUNCTION StudentCount()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;

    SELECT COUNT(*)
    INTO total
    FROM students;

    RETURN total;
END $$

DELIMITER ;

SELECT StudentCount();