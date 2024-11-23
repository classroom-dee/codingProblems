-- 코드를 입력하세요
select a.category, sum(b.sales) as total_sales
from book a
join book_sales b
on a.book_id = b.book_id
where substring(b.sales_date, 1, 7) = '2022-01'
group by a.category
order by a.category asc;

# select sum(sales)
# from book_sales;