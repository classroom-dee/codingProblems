select fh.flavor
from first_half fh
join (
    select shipment_id, flavor, sum(total_order) as jt
    from july
    group by flavor
) j
on fh.shipment_id = j.shipment_id
group by fh.flavor
order by max(fh.total_order + j.jt) desc
limit 3