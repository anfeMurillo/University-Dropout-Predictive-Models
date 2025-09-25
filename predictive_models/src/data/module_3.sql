CREATE TABLE repetitions AS
WITH temporary AS (
    SELECT DISTINCT 
    CODIGO_ID AS id,
    CODIGO_MATERIA AS subject,
    COUNT(CODIGO_MATERIA) 
    OVER 
    (PARTITION BY CODIGO_ID,CODIGO_MATERIA) AS repetitions
FROM Materias_Inscritas
WHERE 
    CAST(CODIGO_ID AS TEXT) 
    IN 
    (SELECT CAST(ID_ESTUDIANTE AS TEXT) FROM Estudiantes_Info)
ORDER BY CODIGO_ID)

SELECT
    DISTINCT
    id,
       SUM(CASE
           WHEN repetitions = 1 THEN 0
           WHEN repetitions != 1 THEN repetitions - 1
           END)
           OVER
               (PARTITION BY id)
           AS total_repetitions
FROM temporary;

INSERT INTO repetitions (id,total_repetitions)
SELECT id,
       0
FROM students
WHERE id NOT IN (SELECT id FROM repetitions);