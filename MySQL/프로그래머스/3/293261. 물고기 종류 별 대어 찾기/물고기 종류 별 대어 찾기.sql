select rnk.id, rnk.fish_name, rnk.length
from (
    select
        i.id,
        i.length,
        ni.fish_name,
        rank() over (partition by i.fish_type order by i.length desc) as h
    from
        fish_info i
    join fish_name_info ni
    on i.fish_type = ni.fish_type
    ) rnk
where rnk.h = 1
order by rnk.id asc