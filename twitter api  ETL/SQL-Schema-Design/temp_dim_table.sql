CREATE TABLE IF NOT EXISTS dim_temp_table
(
  dkey INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `desc`  VARCHAR(50),
  `name` VARCHAR(50)
);

SELECT * FROM dim_temp_table;