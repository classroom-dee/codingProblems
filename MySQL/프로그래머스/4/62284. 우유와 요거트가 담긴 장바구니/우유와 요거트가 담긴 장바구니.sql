with subq as (
select cart_id, group_concat(name separator ', ') as cat
from cart_products 
group by cart_id
)
select cart_id
from subq
where cat like '%Milk%' and cat like '%Yogurt%'
order by cart_id