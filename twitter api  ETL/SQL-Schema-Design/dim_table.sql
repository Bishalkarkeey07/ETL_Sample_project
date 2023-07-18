DROP TABLE IF EXISTS dim_table;

CREATE TABLE IF NOT EXISTS dim_table
(
  dkey INT,
  `name` VARCHAR(50),
  `desc` VARCHAR(50)
);
