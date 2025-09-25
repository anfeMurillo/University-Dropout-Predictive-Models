CREATE TABLE target AS
SELECT
    id,
    CASE
        WHEN total_absences >= 2 THEN 1
    ELSE 0
    END AS deserter
FROM absences;

CREATE TABLE data AS

WITH temporary_3 AS (

WITH temporary_2 AS (

WITH temporary AS (
    
SELECT * FROM final_averages
INNER JOIN target USING (id))

SELECT * FROM repetitions
INNER JOIN temporary USING (id))

SELECT * FROM students
INNER JOIN temporary_2 USING (id))

SELECT COUNT(id) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) AS student_id,* FROM temporary_3;

ALTER TABLE data DROP COLUMN id;