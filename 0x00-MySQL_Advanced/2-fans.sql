-- An SQL script that ranks country origin of
-- bands, ordered by the number of
-- (non-unique fans)
-- The table name is metal_bands
-- Column names must be origin and nb_fans
-- The script is executable on any database
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
