select mcdp_cd, count(apnt_no) as shits_went_down
from appointment
where apnt_ymd between '2022-05-01' and  '2022-05-31'
group by mcdp_cd
order by shits_went_down asc, mcdp_cd asc