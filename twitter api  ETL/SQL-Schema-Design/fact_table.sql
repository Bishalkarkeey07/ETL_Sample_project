DROP TABLE IF EXISTS fact_table;

CREATE TABLE if not exists fact_table
(
  aId BIGINT,
  verification_status VARCHAR(50),
  details_of_creation TIMESTAMP,
  `desc` VARCHAR(50),
  `name` VARCHAR(50),
  username VARCHAR(50),
  no_of_followers INT,
  no_of_following INT,
  no_of_tweets INT,
  no_of_listing INT
);

SET SQL_SAFE_UPDATES = 0;
DELETE fact_table
from temp_fact
JOIN fact_table ON temp_fact.aID =fact_table.aID AND temp_fact.username = fact_table.username;

SELECT * FROM fact_table;


INSERT INTO fact_table (aId, verification_status, details_of_creation, `desc`, `name`, username, no_of_followers, no_of_following, no_of_tweets, no_of_listing)
SELECT DISTINCT aId, verification_status, details_of_creation, `desc`, `name`, username, no_of_followers, no_of_following, no_of_tweets, no_of_listing
FROM temp_fact;

SELECT * from fact_table;
