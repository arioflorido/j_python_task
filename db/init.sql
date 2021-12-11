CREATE DATABASE recipe_db;
use recipe_db;

CREATE TABLE recipes (
  id INT AUTO_INCREMENT,
  title VARCHAR(80) UNIQUE,
  is_available BOOLEAN DEFAULT 0,
  PRIMARY KEY(id)
);

CREATE TABLE ingredients (
  id INT AUTO_INCREMENT,
  name VARCHAR(40) UNIQUE,
  best_before DATE,
  use_by DATE,
  is_expired BOOLEAN,
  PRIMARY KEY(id)
);

CREATE TABLE recipe_ingredient(
  id INT AUTO_INCREMENT,

  recipe_id INT,
  FOREIGN KEY (recipe_id)
    REFERENCES recipes(id),

  ingredient_id INT,
    FOREIGN KEY (ingredient_id)
      REFERENCES ingredients(id),

  PRIMARY KEY(id),
  UNIQUE(recipe_id, ingredient_id)
);
