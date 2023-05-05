"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaaqoe7avj5o49fl4m0-a.oregon-postgres.render.com",
        database="todo_es40",
        user="root",
        password="ZiFMMZj0mOX9h26UM7VUEjsdvOXIJJJu")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
