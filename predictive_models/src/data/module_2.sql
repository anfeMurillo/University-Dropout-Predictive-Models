CREATE TABLE averages AS
SELECT 
ID_ESTUDIANTE AS id,
PERIODO_ACADEMICO AS period,
PGA AS average 
FROM PGA
WHERE ID_ESTUDIANTE IN (SELECT ID_ESTUDIANTE FROM Estudiantes_Info)
ORDER BY ID_ESTUDIANTE;

UPDATE averages SET period = 202210
WHERE period = 202201;

-- This corrects the students who
-- were in Students but not in PGA

DELETE FROM students
WHERE id NOT IN (
SELECT DISTINCT id FROM averages
WHERE id IN (SELECT id FROM students));

CREATE VIEW final_averages AS
WITH temporary AS (
SELECT id,
       COUNT(period) 
       OVER 
       (PARTITION BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) AS semester_number,
       average
FROM averages)

SELECT
    id,
    COALESCE(MAX(CASE WHEN semester_number = 1 THEN average END),0) AS semester_1,
    COALESCE(MAX(CASE WHEN semester_number = 2 THEN average END),0) AS semester_2,
    COALESCE(MAX(CASE WHEN semester_number = 3 THEN average END),0) AS semester_3,
    COALESCE(MAX(CASE WHEN semester_number = 4 THEN average END),0) AS semester_4,
    COALESCE(MAX(CASE WHEN semester_number = 5 THEN average END),0) AS semester_5,
    COALESCE(MAX(CASE WHEN semester_number = 6 THEN average END),0) AS semester_6,
    COALESCE(MAX(CASE WHEN semester_number = 7 THEN average END),0) AS semester_7,
    COALESCE(MAX(CASE WHEN semester_number = 8 THEN average END),0) AS semester_8,
    COALESCE(MAX(CASE WHEN semester_number = 9 THEN average END),0) AS semester_9,
    COALESCE(MAX(CASE WHEN semester_number = 10 THEN average END),0) AS semester_10,
    COALESCE(MAX(CASE WHEN semester_number = 11 THEN average END),0) AS semester_11,
    COALESCE(MAX(CASE WHEN semester_number = 12 THEN average END),0) AS semester_12,
    COALESCE(MAX(CASE WHEN semester_number = 13 THEN average END),0) AS semester_13,
    COALESCE(MAX(CASE WHEN semester_number = 14 THEN average END),0) AS semester_14,
    COALESCE(MAX(CASE WHEN semester_number = 15 THEN average END),0) AS semester_15,
    COALESCE(MAX(CASE WHEN semester_number = 16 THEN average END),0) AS semester_16,
    COALESCE(MAX(CASE WHEN semester_number = 17 THEN average END),0) AS semester_17,
    COALESCE(MAX(CASE WHEN semester_number = 18 THEN average END),0) AS semester_18,
    COALESCE(MAX(CASE WHEN semester_number = 19 THEN average END),0) AS semester_19,
    COALESCE(MAX(CASE WHEN semester_number = 20 THEN average END),0) AS semester_20

FROM temporary
GROUP BY id;