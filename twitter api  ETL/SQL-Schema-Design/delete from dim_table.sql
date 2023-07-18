DELETE dim_table
FROM dim_table
JOIN temp_stage t ON dim_table.`name` = t.`name` AND dim_table.`desc` = t.`desc`;