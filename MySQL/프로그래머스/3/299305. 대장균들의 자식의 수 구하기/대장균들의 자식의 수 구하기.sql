select b.id, count(a.id) as child_count
from ecoli_data a -- child
right join ecoli_data b -- parent
on a.parent_id = b.id
group by b.id
order by b.id