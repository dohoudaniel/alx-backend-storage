-- An SQL script that creates a table
-- 'users' following these requirements:
-- id: An integer, never null, auto increment and a primary key
-- email: A string(255 characters), never null, and unique
-- name: A string(255 characters)
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
