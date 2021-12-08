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
  ('Ham and Cheese Sandwich'),
  ('Big Breakfast'),
  ('Salad'),
  ('Hotdog');

INSERT INTO ingredients
  (name, best_before, use_by, recipe_id)
VALUES
  ('Ham', '2021-12-10', '2021-12-12', 1),
  ('Cheese', '2021-12-11', '2021-12-13', 1),
  ('Bread', '2021-12-12', '2021-12-15', 1),
  ('Butter', '2021-12-10', '2021-12-12', 1),

  ('Bacon', '2021-12-10', '2021-12-12', 2),
  ('Eggs', '2021-12-10', '2021-12-12', 2),
  ('Baked Beans', '2021-12-10', '2021-12-12', 2),
  ('Mushrooms', '2021-12-10', '2021-12-12', 2),
  ('Sausage', '2021-12-10', '2021-12-12', 2),
  ('Bread', '2021-12-12', '2021-12-15', 2),

  ('Lettuce', '2021-12-10', '2021-12-12', 3),
  ('Tomato', '2021-12-10', '2021-12-12', 3),
  ('Cucumber', '2021-12-10', '2021-12-12', 3),
  ('Beetroot', '2021-12-10', '2021-12-12', 3),
  ('Salad Dressing', '2021-12-10', '2021-12-12', 3),

  ('Hotdog Bun', '2021-12-10', '2021-12-12', 4),
  ('Sausage', '2021-12-10', '2021-12-12', 4),
  ('Ketchup', '2021-12-10', '2021-12-12', 4),
  ('Mustard', '2021-12-10', '2021-12-12', 4);

-- TODO Create Shelf life table?
