select
    user.user_id, 
    user.nickname, 
    sum(price) as total_sales
from
    used_goods_board board
    join used_goods_user user
    on board.writer_id = user.user_id
where board.status = 'done'
group by board.writer_id
having total_sales >= 700000
order by total_sales asc;