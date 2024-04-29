from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mongodb_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
mongodb_domain = config.get('DB', 'domain')
db_name = config.get('DB', 'db_name')

URI = (
    f'mongodb+srv://{mongodb_user}:{mongodb_pass}'
    f'@{mongodb_domain}/?retryWrites=true&'
    'w=majority&appName=Cluster0'
)

def create_connect():
    """
    Creates a connection with the MongoDB.
    """
    connect(db=db_name, host=URI, ssl=True)
    print("Successfully connected to MongoDB.")