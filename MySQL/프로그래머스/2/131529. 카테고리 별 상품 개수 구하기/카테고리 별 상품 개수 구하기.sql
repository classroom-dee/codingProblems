select substring(product_code, 1, 2) as shit, count(substring(product_code, 1, 2)) as shit_count
from product
group by shit
order by shit asc