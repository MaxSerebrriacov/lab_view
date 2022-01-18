insert into lab_view.positive (x) select 10 + random() * 10 from generate_series(1, 10000);
update fn set y = sin(x);