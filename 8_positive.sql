drop view positive;
create view positive as
select x , y from lab_view.fn where y > 0.0;