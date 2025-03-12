with recursive timeofday as (
select 0 as t
union all
select t + 1 from timeofday where t < 23)

select tod.t as HOUR, coalesce(count(ao.animal_id), 0) as COUNT
from animal_outs ao
right join timeofday tod
on extract(hour from ao.datetime) = tod.t
group by tod.t
order by HOUR asc