db = db.getSiblingDB("college_db");

db.departments.insertMany([
{
    department_id:1,
    dept_name:"Computer Science",
    head_of_dept:"Dr. Ravi Kumar",
    budget:500000
},
{
    department_id:2,
    dept_name:"Electronics",
    head_of_dept:"Dr. Priya Sharma",
    budget:400000
},
{
    department_id:3,
    dept_name:"Mechanical",
    head_of_dept:"Dr. Arun Kumar",
    budget:350000
}
])

db.students.insertMany([
{
    student_id:1,
    first_name:"Prasanna",
    last_name:"I",
    email:"prasanna@gmail.com",
    department_id:1,
    enrollment_year:2024
},
{
    student_id:2,
    first_name:"Anita",
    last_name:"Reddy",
    email:"anita@gmail.com",
    department_id:1,
    enrollment_year:2021
},
{
    student_id:3,
    first_name:"Kiran",
    last_name:"Kumar",
    email:"kiran@gmail.com",
    department_id:2,
    enrollment_year:2022
},
{
    student_id:4,
    first_name:"Sneha",
    last_name:"Patel",
    email:"sneha@gmail.com",
    department_id:3,
    enrollment_year:2021
},
{
    student_id:5,
    first_name:"Vijay",
    last_name:"Singh",
    email:"vijay@gmail.com",
    department_id:2,
    enrollment_year:2023
}
])

db.courses.insertMany([
{
    course_id:1,
    course_name:"Database Systems",
    course_code:"CS101",
    credits:4
},
{
    course_id:2,
    course_name:"Data Structures",
    course_code:"CS102",
    credits:4
},
{
    course_id:3,
    course_name:"Digital Electronics",
    course_code:"EC201",
    credits:3
}
])

db.students.find()

db.students.find(
{
    department_id:1
})

db.students.updateOne(
{
    first_name:"Prasanna"
},
{
    $set:
    {
        enrollment_year:2025
    }
})

db.students.deleteOne(
{
    first_name:"Vijay"
})

db.students.find()

db.students.countDocuments()

db.students.find().sort(
{
    first_name:1
})


db.students.find(
{},
{
    first_name:1,
    email:1,
    _id:0
})