create rule prevent_updates as on update to fn_backup
do instead nothing;
update fn_backup set y = 0;