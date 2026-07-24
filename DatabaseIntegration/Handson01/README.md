# Hands-on 1 – Schema Design & Core SQL

## Objective
This hands-on focuses on designing and creating the database schema for the Student Course Registration System using MySQL.

## Database Name
college_db

## Topics Covered
- Database Creation
- CREATE TABLE
- PRIMARY KEY
- FOREIGN KEY
- NOT NULL
- UNIQUE Constraint
- CHECK Constraint
- ALTER TABLE
- Referential Integrity
- Database Normalization (1NF, 2NF, 3NF)

## Tables Created
1. departments
2. students
3. courses
4. enrollments
5. professors

## Alter Operations Performed
- Added phone_number column to students
- Added max_seats column to courses
- Added CHECK constraint on grade
- Renamed hod_name to head_of_dept
- Dropped phone_number column

## Verification
- Verified tables using SHOW TABLES
- Verified table structure using DESC command

## Outcome
Successfully created the college_db database with all required tables, constraints, and schema modifications.