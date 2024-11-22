select shit.animal_id, shit.name, date_format(shit.datetime, '%Y-%m-%d') as shat_date
from animal_ins shit
order by shit.animal_id asc