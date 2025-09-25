CREATE VIEW credits AS

WITH temporary AS (

SELECT 
    CODIGO_ID AS id,
    PERIODO AS period,
    CREDITOS_ASIGNATURA AS credits,
    "NOTA FINAL" AS grade 
FROM Materias_Inscritas
    WHERE CODIGO_ID 
    IN 
        (SELECT id FROM students) 
        AND 
        ("NOTA FINAL" > '2.9' OR "NOTA FINAL" IN ('A','CA'))
ORDER BY CODIGO_ID,PERIODO)

SELECT
    DISTINCT
    id,
    period,
    SUM(credits)
        OVER
            (PARTITION BY id,period)
        AS approved_credits
FROM temporary
ORDER BY id,period;

CREATE VIEW temporary_status AS

WITH temporary_2 AS (
WITH temporary AS (
SELECT
    DISTINCT period
FROM averages
WHERE period 
    IN 
    (SELECT DISTINCT start_period FROM students)
ORDER BY period)

SELECT id,start_period,T.period FROM students E
LEFT JOIN temporary T
ORDER BY id)

SELECT * FROM temporary_2 T
LEFT JOIN credits C USING (id,period)
ORDER BY id,period;

CREATE TABLE absences AS
WITH temporary_2 AS (
WITH temporary AS (
SELECT
    *,
    SUM(approved_credits)
    OVER
        (PARTITION BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) AS credit_sum
FROM temporary_status)
SELECT
    *,
    SUM
    (
    CASE
        WHEN start_period > period THEN 0
        WHEN start_period = period THEN 0
        WHEN (start_period < period) AND (approved_credits ISNULL ) AND (credit_sum < 170 OR credit_sum ISNULL ) THEN 1
        ELSE 0
    END
    )
        OVER (PARTITION BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW )
        AS absences
FROM temporary)

SELECT
    DISTINCT
    id,
    MAX(absences) OVER (PARTITION BY id) AS total_absences
FROM temporary_2;