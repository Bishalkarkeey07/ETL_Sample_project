insert into dim_table (dkey,`name`, `desc`)
select dtt.dkey,t.`name`, t.`desc`
from temp_stage t
inner join dim_temp_table dtt
on t.`name` = dtt.`name`
 and t.`desc` = dtt.`desc`;
 
 select * from dim_table;