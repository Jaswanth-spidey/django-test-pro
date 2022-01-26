create database myfirsttarget;
use myfirsttarget;
select database();

desc crudexample_userdetails;
select * from crudexample_userdetails;

insert into crudexample_userdetails(first_name)
values ('Cardinal'), ('Tom B. Erichsen')
,('Skagen 21'), ('Stavanger'), ('4006'), ('Norway');

select * from crudexample_userdetails;

delete from crudexample_userdetails where id>7;
