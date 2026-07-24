USE college_db;

SELECT * FROM students;

SELECT * FROM courses;

SELECT * FROM enrollments;

EXPLAIN
SELECT *
FROM students
WHERE email='prasanna@gmail.com';

CREATE INDEX idx_email
ON students(email);

SHOW INDEX
FROM students;
EXPLAIN
SELECT *
FROM students
WHERE email='prasanna@gmail.com';

CREATE INDEX idx_course_code
ON courses(course_code);

SHOW INDEX
FROM courses;

EXPLAIN
SELECT *
FROM courses
WHERE course_code='CS101';

EXPLAIN
SELECT
    s.first_name,
    c.course_name,
    e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id
WHERE s.first_name='Prasanna';

EXPLAIN
SELECT
    department_id,
    COUNT(*) AS total_students
FROM students
GROUP BY department_id;

EXPLAIN
SELECT *
FROM students
ORDER BY first_name;

SHOW INDEX FROM students;
SHOW INDEX FROM courses;