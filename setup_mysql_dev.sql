CREATE DATABASE IF NOT EXISTS moda_facile_dev_DB;
CREATE USER IF NOT EXISTS 'michael'@'localhost' IDENTIFIED BY 'moda_pass';
GRANT ALL PRIVILEDGES ON moda_facile_dev_DB.* TO 'michael'@'localhost';
