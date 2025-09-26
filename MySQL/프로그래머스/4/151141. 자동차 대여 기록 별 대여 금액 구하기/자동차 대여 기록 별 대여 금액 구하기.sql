# WITH DP AS (
#     SELECT CAR_TYPE, SUBSTRING_INDEX(DURATION_TYPE, '일', 1) AS DC_TYPE, DISCOUNT_RATE
#     FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
# )
# SELECT C.HISTORY_ID, 
#     # C.DAILY_FEE, DP.DISCOUNT_RATE,
#     FLOOR(C.DAILY_FEE * (1 - COALESCE(DP.DISCOUNT_RATE, 0) / 100)) * C.DURATION AS FEE
# FROM (
#     SELECT 
#         CRH.HISTORY_ID, CRH.CAR_TYPE, CRH.DAILY_FEE, CRH.DURATION,
#         CASE
#             WHEN CRH.DURATION BETWEEN 0 and 6 THEN '0'
#             WHEN CRH.DURATION BETWEEN 7 and 29 THEN '7'
#             WHEN CRH.DURATION BETWEEN 30 and 89 THEN '30'
#             ELSE '90'
#         END AS DISCOUNT
#     FROM (
#         SELECT C.CAR_ID, C.CAR_TYPE, C.DAILY_FEE, RH.HISTORY_ID, RH.END_DATE - RH.START_DATE AS DURATION
#         FROM CAR_RENTAL_COMPANY_CAR C
#         JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY RH
#         ON C.CAR_ID = RH.CAR_ID
#         WHERE C.CAR_TYPE='트럭'
#     ) CRH
# ) C LEFT JOIN DP ON C.CAR_TYPE = DP.CAR_TYPE and C.DISCOUNT = DP.DC_TYPE
# ORDER BY
# FEE DESC, C.HISTORY_ID DESC

# Use trim + regex + safe casting
WITH dp AS (
  SELECT
    car_type,
    CAST(TRIM(REGEXP_SUBSTR(duration_type, '^[0-9]+')) AS UNSIGNED) AS threshold,
    discount_rate
  FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
),
crh AS (
  SELECT
    rh.history_id,
    c.car_type,
    c.daily_fee,
    GREATEST(DATEDIFF(rh.end_date, rh.start_date) + 1, 1) AS duration
  FROM CAR_RENTAL_COMPANY_CAR c
  JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY rh
    ON c.car_id = rh.car_id
  WHERE c.car_type = '트럭'
),
graded AS (
  SELECT
    history_id, car_type, daily_fee, duration,
    CASE
      WHEN duration BETWEEN 7 AND 29 THEN 7
      WHEN duration BETWEEN 30 AND 89 THEN 30
      WHEN duration >= 90 THEN 90
      ELSE 0
    END AS threshold
  FROM crh
)
SELECT
  g.history_id,
  FLOOR(g.daily_fee * g.duration * (1 - COALESCE(dp.discount_rate, 0) / 100)) AS fee
FROM graded g
LEFT JOIN dp
  ON dp.car_type = g.car_type
 AND dp.threshold = g.threshold
ORDER BY fee DESC, g.history_id DESC;

