CREATE TABLE users (
  id INT PRIMARY KEY,
  username VARCHAR(50) UNIQUE,
  name VARCHAR(50),
  surname VARCHAR(50),
  email VARCHAR(100) UNIQUE,
  pass VARCHAR(100),
  role INT,
  FOREIGN KEY (role) REFERENCES role(role)
);

CREATE TABLE role (
  id INT PRIMARY KEY,
  role VARCHAR(50)
);

CREATE TABLE results (
  id INT PRIMARY KEY,
  query VARCHAR(100),
  result VARCHAR(100),
  username VARCHAR(50),
  FOREIGN KEY (username) REFERENCES users(username)
);
