-- An SQL script that lists all
-- the bands with 'Glam Rock' as
-- their main style, ranked by
-- their longevity.
-- Column names must be: 'band_name' and 'lifespan'
--      (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
-- Use attributes 'formed' and 'split' to calculate the lifespan
SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
