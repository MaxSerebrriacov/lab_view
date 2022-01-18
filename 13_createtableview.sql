create table positive_tab(x float, y float);
create rule "_RETURN" as on select to positive_tab do instead
select * from fn where y > 0.0;