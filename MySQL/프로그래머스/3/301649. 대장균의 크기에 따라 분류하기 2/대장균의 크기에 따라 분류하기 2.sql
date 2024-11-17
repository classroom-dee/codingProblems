with rnk as (
    select 
        *,
        percent_rank() over (order by size_of_colony desc) as percentile
    from ecoli_data
)
select
    id,
    case
        when percentile <= 0.25 then 'CRITICAL'
        when percentile <= 0.50 then 'HIGH'
        when percentile <= 0.75 then 'MEDIUM'
        else 'LOW'
    end as colony_name
from rnk
order by id