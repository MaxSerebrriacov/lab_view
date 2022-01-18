create view roots as
select round(x::numeric, 2) as x from fn where abs(y)< 0.0013 order by x;