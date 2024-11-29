select count(fi.id) as fish_count, max(fi.length) as max_length, fi.fish_type
from (select id, fish_type,
      case when length is null then 10 else length end as length from fish_info) fi
group by fi.fish_type
having avg(fi.length) >= 33
order by fi.fish_type asc;

# select fi.fish_type, avg(fi.length) over (partition by fi.fish_type order by fi.length)
# from (select id, fish_type,
#       case when length is null then 10 else length end as length from fish_info) fi