-- Selects best score
SELECT (score>=10) as score FROM second_table GROUP BY name ORDER BY scoreDESC;
