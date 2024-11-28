select e.emp_no, e.emp_name,
    case
        when g.score >= 96 then 'S'
        when g.score >= 90 then 'A'
        when g.score >= 80 then 'B'
        else 'C'
    end as grade,
    case
        when g.score >= 96 then cast(e.sal * 0.2 as signed)
        when g.score >= 90 then cast(e.sal * 0.15 as signed)
        when g.score >= 80 then cast(e.sal * 0.1 as signed)
        else 0
    end as bonus
from hr_employees e
join (
    select emp_no, avg(score) as score
    from hr_grade
    group by emp_no
) as g
on e.emp_no = g.emp_no
order by e.emp_no asc