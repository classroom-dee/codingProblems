select date_format(datetime, '%H') as shit_hour, count(animal_id) as shit
from animal_outs
where date_format(datetime, '%H') between 9 and 19
group by shit_hour
order by shit_hour asc