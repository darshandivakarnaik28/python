-- 1
select ename,hiredate from emp;
-- 2
select ename,job,sal,sal/2 from emp;
-- 3
select ename,job,sal,sal-100 as salary_after_reduce from emp;
-- 4
select ename,sal,hiredate from emp
where hiredate<'2023-01-01';
-- 5
select*from emp
where sal>3000;
-- 6
select e.ename,e.sal,d.deptno from emp e join dept d on e.deptno=d.deptno
where e.sal>2500 and e.sal<4000 and e.deptno=20;
-- 7
select *,sal*12 as annual_salary  from emp
where sal between 2000 and 4000;
-- 8
select * from emp
where job='CLERK' and sal<1600;
-- 9
select ename,job,sal from emp
where ename regexp 'R';
-- 10
select e.ename,e.job,d.deptno from emp e join dept d on e.deptno=d.deptno
where d.deptno!=30;
-- 11
select ename,job,sal from emp 
where  sal>2500 and sal<3500;
-- 12
select ename,hiredate,deptno from emp
where year(hiredate)='2022';
-- 13
select*from emp
where mgr=1002;
-- 14
select ename ,job,sal,sal*12 as annual_salary from emp
where job='MANAGER' OR job='ANALYST';
-- 15
select ename,sal,deptno from emp
where sal like '%00';
-- 16
select ename ,job,hiredate from emp
where ename regexp '^S';
-- 17
select ename ,sal,comm from emp
where comm>sal;
-- 18
select ename,job,sal,sal+sal*(10/100) as hike_salary from emp 
where deptno=20 or deptno=30;
-- 19
select * from emp
where job!='CLERK' and job!='SALESMAN' and sal>2500;
-- 20
select ename,job,sal,deptno from emp 
where deptno =10 or deptno=20
having sal!=3000;

use companydb;
select e.ename,d.dname from emp e natural join dept d ;
