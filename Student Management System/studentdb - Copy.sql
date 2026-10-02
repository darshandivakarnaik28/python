use studentdb;
create table students(
roll_number varchar(20) primary key,
name varchar(25) not NULL,
age int not null,
email varchar(15) not null,
course varchar(10) ,
marks int ,
grade varchar(3));

