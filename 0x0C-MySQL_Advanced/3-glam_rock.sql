-- sql languaje holbsc
SELECT
	band_name,
	ifnull(split, YEAR(CURDATE())) - formed as lifespan
FROM
	metal_bands
WHERE
	style LIKE "%Glam rock%"
ORDER BY
	lifespan DESC;