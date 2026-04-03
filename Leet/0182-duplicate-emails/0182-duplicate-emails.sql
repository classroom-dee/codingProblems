# SET OP MUST WORK !!! DANG IT!!!
-- (SELECT email as Email
-- FROM Person)
-- -
-- (SELEECT UNIQUE(email) as Email
-- FROM Person)
# NOT PYTHON LOL

SELECT email as Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1 # if no null is not guaranteed, use COUNT(*)