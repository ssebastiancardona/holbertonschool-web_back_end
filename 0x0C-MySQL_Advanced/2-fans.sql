-- sql languaje holbsc
SELECT
	origin,
	SUM(fans) as nb_fans
FROM
	metal_bands
group by
	origin
order by
	nb_fans DESC;