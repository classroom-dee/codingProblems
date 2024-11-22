select animal_id, name, if(sex_upon_intake like 'Intact%', 'X', 'O') as pretentious_cruelty
from animal_ins
order by animal_id asc