create materialized view fn_all as select * from fn_file with data;
select count(*), 'file' from fn_file union select count(*), 'mat. view' from fn_all;