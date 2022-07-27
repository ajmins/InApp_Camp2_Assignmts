--AJMI N S
--QUESTION 3
--Given Two tables:
--Employee Table
----------------
--EMPNO ENAME JOB MGR HIREDATE SAL COMMISSION DEPTNO
--7839 KING PRESIDENT - 11/17/1981 5000 10
--7698 BLAKE MANAGER 7839 05-01-1981 2850 30
--7782 CLARK MANAGER 7839 06-09-1981 2450 10
--7566 JONES MANAGER 7839 04-02-1981 2975 20
--7788 SCOTT ANALYST 7566 12-09-1982 3000 20
--7902 FORD ANALYST 7566 12-03-1981 3000 20
--7369 SMITH CLERK 7902 12/17/1980 800 20
--7499 ALLEN SALESMAN 7698 02/20/1981 1600 300 30
--7521 WARD SALESMAN 7698 02/22/1981 1250 500 30
--7654 MARTIN SALESMAN 7698 09/28/1981 1250 1400 30
--7844 TURNER SALESMAN 7698 09-08-1981 1500 30
--7876 ADAMS CLERK 7788 01-12-1983 1100 20
--7900 JAMES CLERK 7698 12-03-1981 950 30
--7934 MILLER CLERK 7782 01/23/1982 1300 10
--Department table
------------------
--DEPTNO DNAME LOC
--10 ACCOUNTING NEW YORK
--20 RESEARCH DALLAS
--30 SALES CHICAGO
--40 OPERATIONS BOSTON
-------------------------------------------------------------------


CREATE TABLE Dept(
    deptno INT NOT NULL PRIMARY KEY,
    dname VARCHAR(20),
    loc VARCHAR(20)
);

CREATE TABLE Emp(
    empno INT NOT NULL PRIMARY KEY,
    ename VARCHAR(20),
    job VARCHAR(20),
    mgr INT,
    hiredate DATE,
    sal MONEY,
    commission MONEY,
	deptno INT NOT NULL FOREIGN KEY REFERENCES Dept(deptno),
);

--Insert Values
INSERT INTO Dept VALUES
    (10, 'ACCOUNTING', 'NEW YORK'),
    (20, 'RESEARCH', 'DALLAS'),
    (30, 'SALES', 'CHICAGO'),
    (40, 'OPERATIONS', 'BOSTON');

INSERT INTO Emp VALUES
    (7839, 'KING', 'PRESIDENT', NULL, '11/17/1981', 5000, NULL, 10),
    (7698, 'BLAKE', 'MANAGER', 7839, '05/01/1981', 2850, NULL, 30),
    (7782, 'CLARK', 'MANAGER', 7839, '06/09/1981', 2450, NULL, 10),
    (7566, 'JONES', 'MANAGER', 7839, '04/02/1981', 2975, NULL, 20),
    (7788, 'SCOTT', 'ANALYST', 7566, '12/09/1982', 3000, NULL, 20),
    (7902, 'FORD', 'ANALYST', 7566, '12/03/1981', 3000, NULL, 20),
    (7369, 'SMITH', 'CLERK', 7902, '12/17/1980', 800,  NULL,20),
    (7499, 'ALLEN', 'SALESMAN', 7698, '02/20/1981', 1600 ,300, 30),
    (7521, 'WARD', 'SALESMAN', 7698, '02/22/1981', 1250 ,500, 30),
    (7654, 'MARTIN', 'SALESMAN', 7698, '09/28/1981', 1250 ,1400, 30),
    (7844, 'TURNER', 'SALESMAN', 7698, '09/08/1981', 1500, NULL, 30),
    (7876, 'ADAMS', 'CLERK', 7788, '01/12/1983', 1100, NULL, 20),
    (7900, 'JAMES', 'CLERK', 7698, '12/03/1981', 950, NULL, 30),
    (7934, 'MILLER', 'CLERK', 7782, '01/23/1982', 1300, NULL, 10);
----------------------------
--QUERIES--
-----------------------------
--1. Report needed: Names of employees who are manager.
--Hint: The names of people who have their own employeeID as the managerID
SELECT ename AS 'Names of employees who are manager' 
	FROM Emp
	WHERE empno = mgr;
	--Names of employees who are manager

--2. List the name of all employees along with their department name and Annual
--Income.
--For each row get the output in the form ‘Every Year Mark of Accounts department
--earns amount 450000’. This output has to come under a heading ‘Annual income
--Report’.
SELECT CONCAT('Every Year ', ename, ' of ' , dname, ' department earns amount ', (sal*12)) AS 'Annual income Report'
FROM Emp
JOIN Dept ON Dept.deptno = Emp.deptno
					--Annual income Report
					--Every Year SMITH of RESEARCH department earns amount 9600.00
					--Every Year ALLEN of SALES department earns amount 19200.00
					--Every Year WARD of SALES department earns amount 15000.00
					--Every Year JONES of RESEARCH department earns amount 35700.00
					--Every Year MARTIN of SALES department earns amount 15000.00
					--Every Year BLAKE of SALES department earns amount 34200.00
					--Every Year CLARK of ACCOUNTING department earns amount 29400.00
					--Every Year SCOTT of RESEARCH department earns amount 36000.00
					--Every Year KING of ACCOUNTING department earns amount 60000.00
					--Every Year TURNER of SALES department earns amount 18000.00
					--Every Year ADAMS of RESEARCH department earns amount 13200.00
					--Every Year JAMES of SALES department earns amount 11400.00
					--Every Year FORD of RESEARCH department earns amount 36000.00
					--Every Year MILLER of ACCOUNTING department earns amount 15600.00


--3. Report needed: Names of departments and names of employees. Names of departments
--in ascending order. Within the same department, employee name should be in the
--descending order

SELECT dname AS 'Department', ename AS 'EmployeeName'
FROM Emp
JOIN Dept ON Dept.deptno = Emp.deptno
ORDER BY dname, ename DESC;
					--Department	EmployeeName
					--ACCOUNTING	MILLER
					--ACCOUNTING	KING
					--ACCOUNTING	CLARK
					--RESEARCH	SMITH
					--RESEARCH	SCOTT
					--RESEARCH	JONES
					--RESEARCH	FORD
					--RESEARCH	ADAMS
					--SALES	WARD
					--SALES	TURNER
					--SALES	MARTIN
					--SALES	JAMES
					--SALES	BLAKE
					--SALES	ALLEN






--4. Find out employee name and departmentname of employees who either works in a Toy
--or Shoe department.
SELECT dname AS 'Department', ename AS 'EmployeeName'
FROM Emp
JOIN Dept ON Dept.deptno = Emp.deptno
WHERE dname = 'Toy' OR dname = 'Shoe'
					--Department	EmployeeName


--5. Report needed: Name concatenated with department, separated by comma and space
--and name column Employee and department.
SELECT CONCAT(ename,', ', dname) AS ' Employee and department'
FROM Emp
JOIN Dept ON Dept.deptno = Emp.deptno
				-- Employee and department
				--SMITH, RESEARCH
				--ALLEN, SALES
				--WARD, SALES
				--JONES, RESEARCH
				--MARTIN, SALES
				--BLAKE, SALES
				--CLARK, ACCOUNTING
				--SCOTT, RESEARCH
				--KING, ACCOUNTING
				--TURNER, SALES
				--ADAMS, RESEARCH
				--JAMES, SALES
				--FORD, RESEARCH
				--MILLER, ACCOUNTING

--6. Write a query to display name, job, department number and department name for
--all employees who work in DALLAS.

SELECT ename, job, Dept.deptno, dname
FROM Emp
JOIN Dept ON Dept.deptno = Emp.deptno
WHERE loc = 'DALLAS'
					--ename	job	deptno	dname
					--SMITH	CLERK	20	RESEARCH
					--JONES	MANAGER	20	RESEARCH
					--SCOTT	ANALYST	20	RESEARCH
					--ADAMS	CLERK	20	RESEARCH
					--FORD	ANALYST	20	RESEARCH


--7. List the names of all employees along with name of managers
SELECT ename, mgr
FROM Emp
					--ename	mgr
					--SMITH	7902
					--ALLEN	7698
					--WARD	7698
					--JONES	7839
					--MARTIN	7698
					--BLAKE	7839
					--CLARK	7839
					--SCOTT	7566
					--KING	NULL
					--TURNER	7698
					--ADAMS	7788
					--JAMES	7698
					--FORD	7566
					--MILLER	7782

--8. Display all employee name, manager number and manager name of all employees
--including King who have no manager.
 SELECT ename, mgr 
	FROM Emp;
						-- ename	mgr
						--SMITH	7902
						--ALLEN	7698
						--WARD	7698
						--JONES	7839
						--MARTIN	7698
						--BLAKE	7839
						--CLARK	7839
						--SCOTT	7566
						--KING	NULL
						--TURNER	7698
						--ADAMS	7788
						--JAMES	7698
						--FORD	7566
						--MILLER	7782

--9. Display employee name, department number and all employees that work in same
--department as a given employee (‘Mathew’). Give each column an appropriate label.
 SELECT ename, Emp.deptno   
	FROM Emp
	JOIN Dept ON Dept.deptno = Emp.deptno
	WHERE dname;

--10. Create a unique listing of all jobs that are in department 30. Include location
--of department 30 in the output.
SELECT DISTINCT job AS 'location of department 30'
	FROM Emp
	JOIN Dept ON Dept.deptno = Emp.deptno
	WHERE Dept.deptno = 30;

				--location of department 30
				--CLERK
				--MANAGER
				--SALESMAN

--11. Display the name of students and the course they are doing


--12. Display the name of student and the batch name


--13. Display the name of student and the course name even if there is no student in
--the course.


--14. Display the name of the customer, the data of order and the items ordered by
--the customer