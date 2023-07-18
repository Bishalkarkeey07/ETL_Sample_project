DROP TABLE IF EXISTS temp_stage;
CREATE TABLE temp_stage AS
SELECT DISTINCT
  CAST(id AS CHAR) AS id,
  CAST(verified AS CHAR(7)) AS verification_status,
  CAST(SUBSTRING_INDEX(created_at, 'T', 1) AS DATETIME) AS details_of_creation,
  CAST(`description` AS CHAR(50)) AS `desc`,
  CAST(`name` AS CHAR(50)) AS `name`,
  username AS username,
  CAST(followers_count  AS SIGNED) AS no_of_followers,
  CAST(following_count  AS SIGNED) AS no_of_following,
  CAST(tweet_count  AS SIGNED) AS no_of_tweets,
  CAST(listed_count  AS SIGNED) AS no_of_listing
FROM twitter_data;

select * from temp_stage;