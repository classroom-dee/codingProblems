select distinct car.car_id
from car_rental_company_car car
join car_rental_company_rental_history history
on car.car_id = history.car_id
where car.car_type = '세단' and substring(history.start_date, 6, 2) = '10'
order by car.car_id desc;