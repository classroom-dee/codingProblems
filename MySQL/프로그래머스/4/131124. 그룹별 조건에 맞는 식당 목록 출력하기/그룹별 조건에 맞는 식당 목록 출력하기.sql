select member_name, rr.review_text, rr.review_date
from member_profile mp
join (
    select member_id, review_text, date_format(review_date, '%Y-%m-%d') as review_date
    from rest_review
    where member_id = (
        select member_id
        from rest_review
        group by member_id
        order by count(review_id) desc
        limit 1
    )
) rr
on mp.member_id = rr.member_id
order by review_date asc, review_text asc