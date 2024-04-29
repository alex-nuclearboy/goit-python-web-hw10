import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_project.settings')
django.setup()

from quotesapp.models import Author, Tag, Quote

from pymongo import MongoClient

import configparser

config = configparser.ConfigParser()
config.read('utils/config.ini')

mongodb_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
mongodb_domain = config.get('DB', 'domain')
db_name = config.get('DB', 'db_name')

URI = (
    f'mongodb+srv://{mongodb_user}:{mongodb_pass}'
    f'@{mongodb_domain}/?retryWrites=true&'
    'w=majority&appName=Cluster0'
)

def get_mongodb():
    # Приклад підключення до віддаленого MongoDB
    client = MongoClient(URI)
    db = client[db_name]  # Назва вашої бази даних
    return db

def import_records():
    
    db = get_mongodb()

    authors = db.authors.find()

    for author in authors:
        Author.objects.get_or_create(
            fullname=author['fullname'],
            birth_date=author['born_date'],
            birth_location=author['born_location'],
            description=author['description']
        )

    quotes = db.quotes.find()

    for quote in quotes:
        tags = []
        for tag in quote['tags']:
            t, *_ = Tag.objects.get_or_create(name=tag)
            tags.append(t)
    
        exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

        if not exist_quote:
            author = db.authors.find_one({'_id': quote['author']})
            a = Author.objects.get(fullname=author['fullname'])
            q = Quote.objects.create(
                quote=quote['quote'],
                author=a,            
            )
            for tag in tags:
                q.tags.add(tag)


if __name__ == "__main__":
    import_records()
