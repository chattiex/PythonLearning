--查看所有数据库
show databases;

--使用数据库
--use 数据库名
use test;

--查看当前使用的数据库
select database();

--创建数据库
--create database 数据库名 charset = utf8
create database 作业 charset = utf8;

--删除数据库
--drop database 数据库名；
drop database 作业;

--查看当前数据库中所有表
show tables;

--创建表
create table students(
    id int primary key,
    name varchar(10),
    age int,
    sex varchar(2),
    hobbies varchar(100)
);

--查看表结构
desc students;

--增加修改表字段
alter table students add birthday datetime;

--修改表字段
alter table students change birthday birth datetime;

--修改表字段
alter table students modify birth datetime not null;

--删除表字段
alter table students drop birth;

--查看表创建语句
show create table students;

--查询语句
select * from students;
select name, age from students;

--插入数据
insert into students values(1,'小麦',16,'女','跳绳');

--修改数据
update students set sex='男' where sex='女';

--删除数据
delete from students where id=3;

--字段别名
select id as 序号, name as 名字, sex as 性别 from students;

--表别名
select s.id,s.name from students as s;

--消除重复行,删除sex中的重复数据行。
select distinct sex from students;

--排序,asc从小到大排列（升序），desc从大到小排序（降序）
select * from students order by id asc;

--聚合函数：总数count(),最大值max(),最小值min(),求和sum(),平均值avg()
--分组group by
--having只能用于group by之后，等同于where
--with rollup在最后一行新增一行，来记录当前列里所有记录的总和
select * from students group by sex;
select sex, group_concat(name) from students group by sex;
select sex, count(*) from students group by sex;
select sex, count(*) from students group by sex having count(*)>2;
select sex, count(*) from students group by sex with rollup;

-- 分页
-- select * from 表名 limit strat, count;

-- 查询前5条数据
select * from students limit 5;

-- 查询id为6-10的数据
select * from students limit 5, 5;

-- 查询id 11-14 的数据
select * from students limit 10, 4;

--1.建一张学生表 包含（id，name，age，sex，hobbies）
create table students(
    id int primary key,
    name varchar(10),
    age int,
    sex varchar(2),
    hobbies varchar(100)
);
--2.增加四条数据
insert into students values (1,'小麦',16,'女','跳绳'),(2,'小明',17,'男','打游戏'),(3,'小红',21,'女','化妆'),(4,'小双',22,'女','读书');
--3.查询表中sex为男的数据
select * from students where sex='男';
--4.删除id =3的数据，
delete from students where id=3;
--5.将sex为女的，修改为男
update students set sex='男' where sex='女';
