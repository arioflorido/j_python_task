CREATE DATABASE recipe_db;
use recipe_db;

CREATE TABLE recipes (
  id int AUTO_INCREMENT,
  title VARCHAR(80),
  PRIMARY KEY(id)
);

CREATE TABLE ingredients (
  id int AUTO_INCREMENT,
  name VARCHAR(40),
  best_before date,
  use_by date,
  PRIMARY KEY(id),

  recipe_id int,
  FOREIGN KEY (recipe_id)
    REFERENCES recipes(id)
);

INSERT INTO recipes
  (title)
VALUES
  ('Ham and Cheese Sandwich');

INSERT INTO ingredients
  (name, best_before, use_by, recipe_id)
VALUES
  ('Bacon', '2021-12-10', '2021-12-12', 1),
  ('Eggs', '2021-12-11', '2021-12-13', 1),
  ('Baked Beans', '2021-12-12', '2021-12-15', 1),
  ('Mushroom', '2021-12-10', '2021-12-12', 1),
  ('Sausage', '2021-12-10', '2021-12-12', 1),
  ('Bread', '2021-12-10', '2021-12-12', 1);

-- TODO Create Shelf life table?
