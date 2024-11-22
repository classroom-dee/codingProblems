select animal_type, count(animal_type) as shit_count
from animal_ins
where animal_type in ('Dog', 'Cat')
group by animal_type
order by animal_type asc