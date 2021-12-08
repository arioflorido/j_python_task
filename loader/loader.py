import json
import argparse

FILE_TYPE = (
    'recipes',
    'ingredients'
)

def main():
    parser = argparse.ArgumentParser(description='Recipe & Ingredients Loader')
    parser.add_argument('file_type', help='File Type', choices=FILE_TYPE)
    parser.add_argument('--infile', help='File to load', required=True)
    args = vars(parser.parse_args())

    infile = args['infile']
    with open(infile, 'r') as fh:
        data = json.load(fh)

    if args['file_type'] == 'ingredients':
        load_to_recipes_table(recipe_data=data)
    elif args['file_type'] == 'recipe':
        load_to_ingredients_table(ingredients_data=data)

def load_to_recipes_table(recipe_data):
    pass

def load_to_ingredients_table(ingredients_data):
    pass

main()
