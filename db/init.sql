CREATE DATABASE recipe_db;
use recipe_db;

CREATE TABLE ingredients (
  ingredient_id int AUTO_INCREMENT,
  ingredient_name VARCHAR(40),
  best_before date,
  use_by date,
  PRIMARY KEY(ingredient_id)
);

CREATE TABLE recipes (
  recipe_id int AUTO_INCREMENT,
  recipe_title VARCHAR(80),
  PRIMARY KEY(recipe_id),

  fk_ingredient_id int,
  CONSTRAINT fk_ingredient_id
  FOREIGN KEY (fk_ingredient_id)
    REFERENCES ingredients(ingredient_id)
);

INSERT INTO ingredients
  (ingredient_name, best_before, use_by)
VALUES
  ('Bacon', '2021-12-10', '2021-12-12'),
  ('Eggs', '2021-12-11', '2021-12-13'),
  ('Baked Beans', '2021-12-12', '2021-12-15'),
  ('Mushroom', '2021-12-10', '2021-12-12'),
  ('Sausage', '2021-12-10', '2021-12-12'),
  ('Bread', '2021-12-10', '2021-12-12');

INSERT INTO recipes
  (recipe_title, fk_ingredient_id)
VALUES
  ('Ham and Cheese Sandwich', 1),
  ('Ham and Cheese Sandwich', 2),
  ('Ham and Cheese Sandwich', 3),
  ('Ham and Cheese Sandwich', 4),
  ('Ham and Cheese Sandwich', 5),
  ('Ham and Cheese Sandwich', 6);

