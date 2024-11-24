with babo as (
    select food_type, max(favorites) as favorites
    from rest_info
    group by food_type
)
select 
babo.food_type, rest.rest_id, rest.rest_name, babo.favorites
from rest_info rest
join babo 
on babo.food_type =  rest.food_type
and babo.favorites = rest.favorites
order by babo.food_type desc