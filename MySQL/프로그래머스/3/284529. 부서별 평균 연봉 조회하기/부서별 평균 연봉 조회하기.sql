select
dep.dept_id, dep.dept_name_en, 
round(avg(sal)) as avg_sal
from
hr_department dep
join hr_employees emp
on dep.dept_id = emp.dept_id
group by dep.dept_id
order by avg_sal desc;