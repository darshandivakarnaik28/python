use companydb;
select * from emp;
select * from dept;
select*from mgr;
-- 1
select ename,dname from emp join dept
ON emp.deptno=dept.deptno;

select*from emp;
-- 2
SELECT e.ename,d.loc FROM emp e JOIN dept d
ON e.deptno=d.deptno
where e.job='MANAGER';
-- 3
SELECT e.ename,e.sal,d.dname FROM emp e JOIN dept d
ON e.deptno=d.deptno
where e.job='CLERK' and d.deptno=20 and e.sal>1800;
-- 4
SELECT e.ename,d.deptno,d.dname,d.loc FROM emp e JOIN dept d
ON e.deptno=d.deptno
WHERE e.sal>1400 and d.loc='NEw YORK';
-- 5
select d.dname,e.mgr FROM dept d join emp e
ON d.deptno=e.deptno
where e.mgr=1002;
-- 6
select d.dname,e.empno FROM emp e join dept d
on d.deptno=e.deptno
where d.loc='bangalore' and e.empno in (1001,1010);

-- 7
SELECT e.ename,d.dname from dept d join emp e
on e.deptno=d.deptno;
-- 8
SElect e.ename,e.job,e.sal,d.dname,d.loc from
emp e left join dept d
on e.deptno=d.deptno;

-- 9
select e.ename ,d.dname,
-- ifnull(d.dname,"NO DEPARTMENT") as dname
coalesce(d.dname,d.loc,"NO DEPARTMENT")
from emp e join dept d
on e.deptno=d.deptno;

-- 10
select e.ename,d.dname from emp e right join dept d
on e.deptno=d.deptno;

-- 11
select d.dname,count(e.empno) from 
dept d join emp e
on d.deptno=e.deptno
group by d.deptno;

-- 12
select e.ename,e.sal,d.dname ,d.loc 
from dept d left join emp e
on d.deptno=e.deptno
where d.loc='boston';

-- 13
select d.dname,d.loc,sum(e.sal) from dept d right join
emp e on d.deptno=e.deptno
group by d.deptno
having sum(e.sal)=NULL;

-- 14
select e.ename,e.sal,m.ename,m.sal  from emp e
 left join emp m
 on e.mgr=m.empno;
 
 -- bhaskar sir
 -- 1
 select e1.mgr ,count(e2.empno) from emp e1 join  emp e2
 on e1.mgr=e2.empno
 group by e1.mgr;
