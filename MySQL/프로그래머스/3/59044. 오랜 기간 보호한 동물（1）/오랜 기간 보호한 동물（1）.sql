-- 코드를 입력하세요
select
    ins.name,
    ins.datetime
from
    animal_ins ins
    left join animal_outs outs
    on ins.animal_id = outs.animal_id
where outs.datetime is null
order by ins.datetime asc
limit 3