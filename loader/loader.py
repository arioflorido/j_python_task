import json
import argparse
import os
from DBcm import UseDatabase, CredentialsError, SQLError

DATA_TYPE = (
    'recipes',
    'ingredients'
)

def main():
    parser = argparse.ArgumentParser(description='Recipe & Ingredients Loader')
    parser.add_argument('file_type', help='File Type', choices=DATA_TYPE)
    parser.add_argument('--infile', help='File to load', required=True)
    args = vars(parser.parse_args())

    infile = args['infile']
    with open(infile, 'r') as fh:
        data = json.load(fh)

    if args['file_type'] == 'ingredients':
        load_to_ingredients_table(ingredients_data=data)
    elif args['file_type'] == 'recipes':
        load_to_recipes_table(recipe_data=data)

def load_to_recipes_table(recipe_data):
    try:
        dbconfig = {'host': '127.0.0.1',
                    'user': 'root',
                    'password': 'root',
                    'database': 'recipe_db'}

        with UseDatabase(dbconfig) as cursor:
            _SQL_REPLACE = """
            replace into recipes (name)
            values (%s)
            """
            # # insert statement (with data placeholders)
            # _SQL_INSERT = """insert into log
            #                 (phrase, letters, ip, browser_string, results)
            #                 values (%s, %s, %s, %s, %s)
            #                 """

            recipe = (,)

            # # data to be logged to the database
            # insert_values = (req.form['phrase'], req.form['letters'],
            #                     req.remote_addr, req.user_agent.browser,
            #                     res)

            # cursor.execute(_SQL_INSERT, insert_values)

    except ConnectionError as err:
        print('Is your database switched on? Error: ', str(err))
    except CredentialsError as err:
        print('Database User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))

def load_to_ingredients_table(ingredients_data):
    pass

main()
