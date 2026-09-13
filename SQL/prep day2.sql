-- 1
select sum(sal) as total_sal from emp;
-- 2
select avg(sal),max(sal),min(sal) from emp;
-- 3
select sum(comm) as tortal_commission from emp;
-- 4
select count(empno) as total_employee from emp;
-- 5
select sum(amount) as total_order_amount from orders;
-- 6
select avg(amount) as average_order_amount from orders;
-- 7
select max(amount) as max,min(amount) as min from orders;
-- 8
select deptno ,count(empno) from emp
group by deptno;
-- 9
select deptno,sum(sal) from emp 
group by deptno;
-- 10
select deptno,avg(sal) from emp
group by deptno;
-- 11
select deptno,max(sal) from emp
group by deptno;
-- 12
select job,count(empno) from emp
group by job;
-- 13 
select job,sum(sal) from emp
group by job;
-- 14
select job,avg(sal),max(sal),min(sal) from emp
group by job;
-- 15
select mgr,count(empno) from emp
group by mgr;
-- 16
select status,count(order_id) from orders
group by status;
-- 17
select status,sum(amount) from orders 
group by status;
-- 18
select empno,sum(amount) from orders 
group by empno;
-- 19
select cid,count(order_id) from orders
where status='DELIVERED'
group by cid;
-- 20
select cid,sum(amount) from orders
group by cid;
-- 21
select deptno,sum(sal) from emp
group by deptno
having sum(sal)>7000;
-- 22
select job,avg(sal) from emp
group by job
having avg(sal)>2500;
-- 23
select deptno,count(empno) from emp
group by deptno
having count(empno)>2;
-- 24
select status,sum(amount) from orders
group by status
having sum(amount)>50000;
-- 25
select empno,sum(amount) from orders
group by empno
having sum(amount)>30000;
-- 26
select ename,job,sal,deptno from emp
order by sal desc;
-- 27
select ename,job,sal,deptno from emp
order by sal desc
limit 5;
-- 28
select order_id,cid,empno,amount,status from orders
where status="DELIVERED"
order by amount desc
limit 3;
-- 29
select ename,job,sal,deptno from emp
order by sal asc
limit 5;
-- 30
select empno,sum(amount) from orders
group by empno
order by sum(amount) desc
limit 3;
