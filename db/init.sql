CREATE DATABASE recipe_db;
use recipe_db;

CREATE TABLE recipes (
  id int AUTO_INCREMENT,
  title VARCHAR(80) UNIQUE,
  PRIMARY KEY(id)
);

CREATE TABLE ingredients (
  id int AUTO_INCREMENT,
  name VARCHAR(40) UNIQUE,
  best_before date,
  use_by date,
  PRIMARY KEY(id)
);

CREATE TABLE recipe_ingredient(
  id int AUTO_INCREMENT,

  recipe_id int,
  FOREIGN KEY (recipe_id)
    REFERENCES recipes(id),

  ingredient_id int,
    FOREIGN KEY (ingredient_id)
      REFERENCES ingredients(id),

  PRIMARY KEY(id)
);
