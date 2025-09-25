-- Creation of the temporary students table.

CREATE TABLE students as

SELECT ID_ESTUDIANTE as id,
       EDAD as age,
       GENERO as gender,
       ESTRATO as stratum,
       RESIDENCIA as residence,
       DESC_ESTADO_CIVIL as civil_status,
       PERIODO_CATALOGO as start_period
FROM Estudiantes_Info;

UPDATE students SET residence = CASE
    WHEN residence LIKE ('%CALI%') THEN '0'
    WHEN residence LIKE ('CANDELARIA') THEN '1'
    WHEN residence LIKE ('JAMUND%') THEN '1'
    WHEN residence LIKE ('YUMBO') THEN '1'
    WHEN residence LIKE ('PALMIRA') THEN '1'
    WHEN residence LIKE ('DAGUA') THEN '1'
    ELSE '2'
END;

UPDATE students SET gender = CASE
    WHEN gender = 'F' THEN '2'
    WHEN gender = 'M' THEN '1'
    WHEN gender = 'N' THEN '0'
END;

UPDATE students SET civil_status = CASE
    WHEN civil_status = 'Soltero(a)' THEN '0'
    WHEN civil_status = 'U libre' THEN '1'
    WHEN civil_status = 'Casado(a)' THEN '2'
END;

UPDATE students SET stratum = CASE
    WHEN stratum =  0 THEN (SELECT CEILING (AVG(stratum)) from students)
    ELSE stratum
END;

UPDATE students SET start_period = 202210
WHERE start_period = 202201;

UPDATE students SET start_period = 202310
WHERE start_period = 202301;