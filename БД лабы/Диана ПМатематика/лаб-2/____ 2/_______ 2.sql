create table if not exists Department(
	depart_id serial primary key,
	Name varchar(30) not null
);
	
create table if not exists Positions(
	pos_id serial primary key,
	name varchar(30)
);

create table if not exists Employees(
	emp_id serial primary key,
	name varchar(30),
	salary int,
	premium int,
	depart_id int references Department(depart_id),
	pos_id int references Positions(pos_id)
);

insert into department(name) values
('Отдел_продаж'),('Отдел_рекламы'),('бухгалтерия'),('ИТ_отдел');

insert into positions(name) values
('руководитель отдела'),('старший специалист'),('специалист'),('главный бухгалтер'),
('бухгалтер'),('системный администратор'),('генеральный директор'),('финансовый директор');


insert into employees(name,salary,premium,depart_id,pos_id) values
('Виктор',250000,0,null,7),('Андрей',170000,0,null,8),
('Максим',100000,1,2,1),('Василий',110000,0,4,1),
('Дмитрий',70000,1,4,6),('Артем',70000,0,4,6),
('Алиса',65000,0,3,4),('Диана',45000,1,3,5),
('Алексей',50000,0,3,5),('Никита',60000,1,2,3),
('Дмитрий',65000,0,2,3),('Денис',73000,0,1,3),
('Александр',120000,0,1,1),('Николай',80000,1,1,3),
('Евгений',100000,1,1,2);

alter table employees
add check(premium = 0 or premium = 1);
-- пункт 4
-- средняя заработная плата по отделам без учета премий

select d.name,avg(salary) as Средняя_зарплата
from employees e
join department d on  e.depart_id = d.depart_id
group by(d.name);

-- c учетом премии
select d.name,avg(e.salary) as Средняя_зарплата
from (select depart_id, salary +salary/12*premium as salary from employees) e
join department d on  e.depart_id = d.depart_id
group by(d.name);

-- пункт 5

-- средняя зарплата руководителей отделов
select d.name as Руководитель_отдела, avg(e.salary) as Средняя_зарплата
from employees e
join department d on e.depart_id = d.depart_id
where e.pos_id in (select p.pos_id from positions p where p.name = 'руководитель отдела')
group by(d.name);

-- пункт 6

-- минимальная и максимальная зарплата
select min(e.salary) as минимальная_зарплата, max(e.salary) as максимальная_зарплата
from employees e;

-- пункт 7

--сотрудники получающие премиальные выплаты
select e.name
from employees e 
where premium = 1;

-- пункт 8

-- должности в порядке возрастания зарплаты
select p.name, avg(salary) as средняя_зарплата
from employees e 
join positions p on e.pos_id =p.pos_id
group by(p.name)
order by средняя_зарплата;




	