CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(50) NOT NULL,
  surname VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  pass VARBINARY(100) NOT NULL,
  role VARCHAR(50) NOT NULL,
  FOREIGN KEY (role) REFERENCES role(role_name)
);

CREATE TABLE role (
  id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  role_name VARCHAR(50) NOT NULL
);

CREATE TABLE results (
  id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  query VARCHAR(100) NOT NULL ,
  result VARCHAR(100) NOT NULL ,
  username VARCHAR(50) NOT NULL,
  FOREIGN KEY (username) REFERENCES users(username)
);
INSERT INTO users (username, name, surname, email, pass, role)
VALUES ('user1', 'John', 'Doe', 'john.doe@example.com', ENCRYPT('password'), 'admin');
