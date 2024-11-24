-- year, month, gender, users
select s.year, s.month, i.gender, count(distinct i.user_id) as users
from user_info i
join (
    select
    user_id,
    year(sales_date) as year,
    month(sales_date) as month
    from online_sale
) s
on i.user_id = s.user_id
where i.gender is not null
group by s.year, s.month, i.gender

