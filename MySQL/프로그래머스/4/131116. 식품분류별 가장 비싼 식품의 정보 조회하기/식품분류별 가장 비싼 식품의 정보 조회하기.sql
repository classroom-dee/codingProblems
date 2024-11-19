select ranked_pd.category, ranked_pd.price as max_price, ranked_pd.product_name
from (
    select category, price, product_name,
    rank() over (partition by category order by price desc) as rnk
    from food_product
    where category in ('김치', '식용유', '국', '과자')
) ranked_pd
where rnk = 1
order by max_price desc