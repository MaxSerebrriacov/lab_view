create server file_server foreign data  wrapper file_fdw;
create foreign table fn_file(x float, y float) server file_server
options (filename '/home/user/lab_view/sine.csv', format 'csv');