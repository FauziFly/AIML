--create object objectName

create database OurDB
--create table <TableName>
--ColumnName DataType <constraint>

use OurDB
create table Student
(SId int primary key,
SName nvarchar(50) not null,
SFee float not null)

select * from Student
insert into Student values (1,'Sam',5000.50)
insert into Student values 
(2,'Rohit',4500.50),
(3,'Neha',5000.60),
(4,'Shui',4900.00),
(5,'Drouy',6000.00)