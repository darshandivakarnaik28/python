-- 1
select * from emp
where sal >(select avg(sal) from emp);
-- 2 
select ename,job,sal,deptno from emp
where sal =(select max(sal) from emp);
-- 3
select ename,job,sal,deptno from emp
where sal=(select min(sal) from emp);
-- 4
select ename,job,sal,deptno from emp
where sal>(select sal from emp where ename like '%RAJ%');
-- 5
select ename,hiredate,job,sal from emp
where hiredate <(select hiredate from emp where ename like '%KIRAN%');
-- 6
select ename,job,sal,deptno from emp
where ename in (select ename from emp where job="ANALYST"); 
-- 7
select ename,job,sal,deptno from emp
where sal in (select sal from emp where job="CLERK" );
-- 8
select e.ename,e.job,e.sal,e.deptno from emp e join dept d
on e.deptno=d.deptno
where loc="BANGALORE" or loc= "PUNE";
 -- 9
 select * from orders
 where  status="DELIVERED";
 -- 10
 select e.empno,e.ename,e.job,e.hiredate,e.mgr,e.sal,e.comm,e.deptno from emp e join orders o
 on e.empno=o.empno
 where amount>25000;
 
 select * from emp e,orders o
 where e.empno=o.empno and amount>25000;
 
 select * from orders;
 
 