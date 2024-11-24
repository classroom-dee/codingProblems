select
user.user_id, user.nickname,
concat(user.city, ' ', user.street_address1, ' ', user.street_address2) as 전체주소,
insert(insert(insert(tlno, 4, 0, '-'), 9, 0, '-'), 14, 0, '-') as 전화번호
from
USED_GOODS_BOARD board
join
USED_GOODS_USER user
on user.user_id = board.writer_id
group by user.user_id
having count(board.writer_id) >= 3
order by user.user_id desc;