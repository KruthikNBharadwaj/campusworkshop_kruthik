"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaahlm7avj5o48ushtg-a.oregon-postgres.render.com",
        database="todo_betsol_g8s2",
        user="root",
        password="2QS6Tr3K7Z4jgn3pnWla3khEAL0wsDrn")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
