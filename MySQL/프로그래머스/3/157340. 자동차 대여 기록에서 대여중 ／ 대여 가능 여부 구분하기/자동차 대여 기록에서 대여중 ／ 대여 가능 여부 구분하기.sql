with cav as
(
select
    car_id,
    case
        when '2022-10-16' between start_date and end_date then 0
        else 1
    end as availability
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)
select
car_id,
case
    when sum(availability) = count(*) then '대여 가능'
    else '대여중'
end as availability
from cav
group by car_id
order by car_id desc;