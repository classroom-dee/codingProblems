with recursive ecol_gen as (
    select id, parent_id, 1 as gen
    from ecoli_data
    where parent_id is null
    
    union all
    
    select ed.id, ed.parent_id, eg.gen + 1
    from ecoli_data ed
    join ecol_gen eg on ed.parent_id = eg.id
    where eg.gen < 3 # stop at 2 + 1
)
select id from ecol_gen
where gen = 3
order by id asc