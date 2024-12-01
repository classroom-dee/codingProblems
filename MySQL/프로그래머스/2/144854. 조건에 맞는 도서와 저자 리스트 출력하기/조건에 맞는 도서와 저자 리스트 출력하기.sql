select A.book_id, B.author_name, date_format(A.published_date, '%Y-%m-%d') as shat_date
from book A join author B
where A.author_id = B.author_id and A.category = '경제'
order by A.published_date asc