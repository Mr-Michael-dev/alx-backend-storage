-- ranks country origins of bands, ordered by the number of (non-unique) fans

-- Create an index on the metal_bands table for easy transversing
DROP INDEX IF EXISTS origin_fans ON metal_bands;
CREATE INDEX origin_fans ON metal_bands (fans, origin);

-- Select origin and fans
SELECT origin, sum(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
