use studentdb;
create table students(
roll_number varchar(10) primary key,
name varchar(10) not NULL,
age int not null,
email varchar(10) not null,
course varchar(10) ,
marks int ,
grade varchar(2));

desc students;
