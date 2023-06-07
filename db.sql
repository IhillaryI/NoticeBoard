CREATE DATABASE IF NOT EXISTS noticeboard;

CREATE USER IF NOT EXISTS
    'noticeboard'@'localhost' IDENTIFIED BY 'Notice_dev_pw9';

GRANT ALL PRIVILEGES ON `noticeboard`.* TO 'noticeboard'@'localhost';
FLUSH PRIVILEGES;
