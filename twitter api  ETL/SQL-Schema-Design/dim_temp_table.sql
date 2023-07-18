insert into dim_temp_table (`desc`,`name`)
select t.`desc`, t.`name` 
from temp_stage t
left join dim_temp_table dtt
on t.`desc` = dtt.`desc` and t.`name` = dtt.`name`
where dtt.`name` is null;

select * from dim_temp_table;