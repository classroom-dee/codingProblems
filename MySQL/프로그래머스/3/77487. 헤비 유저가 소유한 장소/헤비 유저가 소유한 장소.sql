select p.id, p.name, p.host_id
from (
    select host_id,
    case
        when count(id) >= 2 then true
        else false
    end as heavy
    from places
    group by host_id
) hvy
join places p
on hvy.host_id = p.host_id
where hvy.heavy is true
order by p.id;