CREATE DATABASE recipe_db;
use recipe_db;

CREATE TABLE recipes (
  id INT AUTO_INCREMENT NOT NULL,
  title VARCHAR(80) UNIQUE NOT NULL,
  is_fresh BOOLEAN NOT NULL DEFAULT 1,
  is_available BOOLEAN NOT NULL DEFAULT 1,
  PRIMARY KEY(id)
);

CREATE TABLE ingredients (
  id INT AUTO_INCREMENT NOT NULL,
  name VARCHAR(40) UNIQUE NOT NULL,
  best_before DATE NOT NULL,
  use_by DATE NOT NULL,
  is_expired BOOLEAN NOT NULL DEFAULT 0,
  PRIMARY KEY(id)
);

CREATE TABLE recipe_ingredient(
  id INT AUTO_INCREMENT,

  recipe_id INT NOT NULL,
  FOREIGN KEY (recipe_id)
    REFERENCES recipes(id),

  ingredient_id INT NOT NULL,
    FOREIGN KEY (ingredient_id)
      REFERENCES ingredients(id),

  PRIMARY KEY(id),
  UNIQUE(recipe_id, ingredient_id)
);
