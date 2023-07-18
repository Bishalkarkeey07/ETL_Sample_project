CREATE TABLE IF NOT EXISTS stage (
  id BIGINT,
  verified VARCHAR(50),
  created_at TIMESTAMP,
  `description` VARCHAR(50),
  `name` VARCHAR(50),
  username VARCHAR(50),
  followers_count INT,
  following_count INT,
  tweet_count INT,
  listed_count INT
);

INSERT INTO stage (id,verified,created_at,`description`,`name`,username,followers_count,following_count,tweet_count ,listed_count )
SELECT
 id,
 verified,
 STR_TO_DATE(created_at, '%Y-%m-%dT%H:%i:%s.000Z') AS created_at,
 `description`,
 `name`,
 username,
 followers_count,
 following_count,
 tweet_count,
 listed_count 
FROM twitter_data;

Select * from stage;