# WITH great AS
# (
# SELECT
#     CASE
#         WHEN (nope.cats LIKE '%Front End%') AND (nope.skilz LIKE '%Python%') THEN 'A'
#         WHEN nope.skilz LIKE '%C#%' THEN 'B'
#         WHEN nope.cats LIKE '%Front End%' THEN 'C'
#         ELSE Null
#     END AS grade,
#     nope.id, nope.email
# FROM
#     (
#         SELECT
#             d.id, d.email, 
#             GROUP_CONCAT(DISTINCT s.name) AS skilz, 
#             GROUP_CONCAT(DISTINCT s.category) AS cats
#         FROM
#             developers d
#         JOIN
#             skillcodes s
#         ON
#             d.skill_code & s.code
#         GROUP BY
#             d.id, d.email
#     ) AS nope
# )
# SELECT great.grade, great.id, great.email
# FROM great
# WHERE
#     great.grade is not null
# ORDER BY
#     great.grade asc, great.id asc


# OPTIMIZED
WITH masks AS (
  SELECT
    BIT_OR(CASE WHEN category = 'Front End' THEN code ELSE 0 END) AS m_frontend,
    BIT_OR(CASE WHEN name     = 'Python'   THEN code ELSE 0 END) AS m_python,
    BIT_OR(CASE WHEN name     = 'C#'       THEN code ELSE 0 END) AS m_csharp
  FROM skillcodes
)
SELECT
  CASE
    WHEN (d.skill_code & m.m_frontend) <> 0
     AND (d.skill_code & m.m_python)   <> 0 THEN 'A'
    WHEN (d.skill_code & m.m_csharp)   <> 0 THEN 'B'
    WHEN (d.skill_code & m.m_frontend) <> 0 THEN 'C'
    ELSE NULL
  END AS grade,
  d.id, d.email
FROM developers d
CROSS JOIN masks m
WHERE
      ((d.skill_code & m.m_frontend) <> 0 AND (d.skill_code & m.m_python) <> 0)
   OR  (d.skill_code & m.m_csharp)   <> 0
   OR  (d.skill_code & m.m_frontend) <> 0
ORDER BY grade ASC, d.id ASC;