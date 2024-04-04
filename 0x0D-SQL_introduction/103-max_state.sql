-- max temp by city
SELECT state, MAX(value) AS max_temp FROM temperature GROUP BY city ORDER BY avg_temp DESC;
