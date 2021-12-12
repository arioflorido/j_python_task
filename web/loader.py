from app.database.session import SessionLocal
from app import crud
import json
import argparse
from datetime import date

DATA_TYPE = (
    'recipes',
    'ingredients',
)

db = SessionLocal()
today = date.today()


def main():
    # Example usage
    # python loader.py ingredients --infile input_files/ingredients.json
    # python loader.py recipe --infile input_files/recipe.json
    parser = argparse.ArgumentParser(description='Recipe & Ingredients Loader')
    parser.add_argument('file_type', help='File Type', choices=DATA_TYPE)
    parser.add_argument('--infile', help='File to load', required=True)
    args = vars(parser.parse_args())

    infile = args['infile']
    with open(infile, 'r') as fh:
        data = json.load(fh)

    if args['file_type'] == 'ingredients':
        load_to_ingredients_table(ingredients_data=data['ingredients'])
    elif args['file_type'] == 'recipes':
        load_to_recipes_table(recipe_data=data['recipes'])


def load_to_recipes_table(recipe_data: list):
    # TODO: REFACTOR / ENHANCE
    ingredients = crud.get_ingredients(db)
    if not ingredients:
        print('Error: Load some ingredients first before loading the recipes!')
        return

    for item in recipe_data:
        recipe_data = {
            'title': item['title'],
            'is_fresh': True,
            'is_available': True
            }

        recipe = crud.upsert_recipe(db, recipe_data)

        if not recipe:
            continue

        for ingredient_name in item['ingredients']:
            ingredient = crud.get_ingredient_by_name(db=db, name=ingredient_name)

            # TODO: Logic for checking is_fresh should live in API and not here.
            if ingredient:
                crud.upsert_recipe_ingredient(db, recipe_id=recipe.id, ingredient_id=ingredient.id)
                if recipe_data['is_fresh'] and ingredient.best_before >= today:
                    recipe_data['is_fresh'] = False
            else:
                if recipe_data['is_available']:
                    recipe_data['is_available'] = False

        recipe = crud.upsert_recipe(db, recipe_data)


def load_to_ingredients_table(ingredients_data: list):
    new_mapping = {
        'title': 'name',
        'best-before' : 'best_before',
        'use-by' : 'use_by'
    }

    for item in ingredients_data:
        item = rename_keys(obj=item, new_mapping=new_mapping)
        crud.upsert_ingredient(db, item)


def rename_keys(obj: dict, new_mapping: dict) -> dict:
    for old_key, new_key in new_mapping.items():
        obj[new_key] = obj.pop(old_key)
    return obj


if __name__ == '__main__':
    main()
