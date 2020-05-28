SELECT dt as Data, model as Modelo,
CONCAT(ROUND(((t0*100)/Total),2), '%') as '0%',
CONCAT(ROUND(((t1*100)/Total),2), '%') as '25%',
CONCAT(ROUND(((t2*100)/Total),2), '%') as '50%',
CONCAT(ROUND(((t3*100)/Total),2), '%') as '75%',
CONCAT(ROUND(((t4*100)/Total),2), '%') as '100%',
CONCAT(ROUND(((t5*100)/Total),2), '%') as '>100%'
FROM (
SELECT 
  dt, model,
  SUM(CASE WHEN total = 0 THEN 1 ELSE 0 END) as t0,
  SUM(CASE WHEN total = 1 THEN 1 ELSE 0 END) as t1,
  SUM(CASE WHEN total = 2 THEN 1 ELSE 0 END) as t2,
  SUM(CASE WHEN total = 3 THEN 1 ELSE 0 END) as t3,
  SUM(CASE WHEN total = 4 THEN 1 ELSE 0 END) as t4,
  SUM(CASE WHEN total > 4 THEN 1 ELSE 0 END) as t5,
  COUNT(*) AS Total
FROM medidor
WHERE model LIKE '%E450%'
GROUP BY dt,model) as soma
ORDER BY dt DESC;