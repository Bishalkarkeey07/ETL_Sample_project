DROP TABLE IF EXISTS temp_fact;

CREATE TABLE temp_fact AS
SELECT
    s.id as aId,
    s.`name` as `name`,
    s.`desc` AS `desc`,
    s.verification_status AS verification_status,
    s.details_of_creation AS details_of_creation,
    s.username AS username,
    s.no_of_followers AS no_of_followers,
    s.no_of_following AS no_of_following,
    s.no_of_tweets AS no_of_tweets,
    s.no_of_listing AS no_of_listing
    FROM
    temp_stage s
LEFT JOIN
    dim_table c ON s.`name` = c.`name` and s.`desc` = c.`desc`;
    
select * from temp_fact;