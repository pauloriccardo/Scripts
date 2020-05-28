SELECT 
  dt AS Data, model AS Modelo,
  CONCAT(SUM(CASE WHEN total = 0 THEN 1 ELSE 0 END)) as 'Total sem Entrega',
  CONCAT(SUM(CASE WHEN total = 1 THEN 1 ELSE 0 END)) as '25%',
  CONCAT(SUM(CASE WHEN total = 2 THEN 1 ELSE 0 END)) as '50%',
  CONCAT(SUM(CASE WHEN total = 3 THEN 1 ELSE 0 END)) as '75%',
  CONCAT(SUM(CASE WHEN total = 4 THEN 1 ELSE 0 END)) as '100%',
  CONCAT(SUM(CASE WHEN total > 4 THEN 1 ELSE 0 END)) as '>100%',
  CONCAT(COUNT(*)) as Total
FROM medidor
WHERE model LIKE '%E450%'
GROUP BY dt,model
ORDER BY dt DESC;
