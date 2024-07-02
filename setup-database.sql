--  prepares a MySQL server for the Web_app
CREATE DATABASE IF NOT EXISTS mrt_db;
CREATE USER IF NOT EXISTS 'mrt_user' @'%' IDENTIFIED BY 'menofiart_pwd';
GRANT ALL PRIVILEGES ON `mrt_db`.* TO 'root' @'%';
FLUSH PRIVILEGES;
CREATE TABLE IF NOT EXISTS `sensors` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date DATE,
  time TIME,
  SOC INT CHECK (
    SOC >= 0
    AND SOC <= 100
  ),
  speed INT,
  rpm INT,
  distance_travelled INT,
  Range_Available INT,
  Current FLOAT,
  Voltage FLOAT,
  GPS VARCHAR(60)
);