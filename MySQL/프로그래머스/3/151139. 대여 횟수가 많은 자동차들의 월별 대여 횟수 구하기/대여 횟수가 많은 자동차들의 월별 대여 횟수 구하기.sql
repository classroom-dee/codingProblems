-- 코드를 입력하세요
# select month(rh.start_date) as MONTH, subq.CAR_ID, count(*) as RECORDS
# from car_rental_company_rental_history rh
# join
# (
#     select car_id, count(*) as records
#     from car_rental_company_rental_history
#     where start_date between date '2022-08-01' and date '2022-10-31'
#     group by car_id
#     having records >= 5 
# ) subq
# on rh.car_id = subq.car_id
# group by month, rh.car_id
# having records > 0
# order by month asc, rh.car_id desc

# I'm lost. is it because of the count(*)?
# Are the return types of extract() and month() different?

with subq as (
    select car_id
    from car_rental_company_rental_history
    where start_date between '2022-08-01' and '2022-10-31'
    group by car_id
    having count(history_id) >= 5
)
select 
    extract(month from orig.start_date) as month,
    orig.car_id,
    count(orig.history_id) as records
from car_rental_company_rental_history as orig
join subq
on orig.car_id = subq.car_id
where orig.start_date between '2022-08-01' and '2022-10-31'
group by month(orig.start_date), orig.car_id
having count(orig.history_id) > 0
order by month(orig.start_date) asc, orig.car_id desc