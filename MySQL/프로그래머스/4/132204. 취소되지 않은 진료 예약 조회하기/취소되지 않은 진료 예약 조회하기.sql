select 
a.apnt_no, p.pt_name, p.pt_no,
a.mcdp_cd, d.dr_name, 
a.apnt_ymd
from patient p
join appointment a
on p.pt_no = a.pt_no
join doctor d
on d.dr_id = a.mddr_id
where a.apnt_ymd like '2022-04-13%' 
and a.apnt_cncl_yn = 'N'
and a.mcdp_cd = 'CS'
order by a.apnt_ymd asc