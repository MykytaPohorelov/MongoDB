from pymongo import MongoClient
import json

client = MongoClient('mongodb+srv://mykytapohorelov:Goodwin7471@cluster0.5qnky6f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['quotes_db']

quotes_collection = db['quotes']
authors_collection = db['authors']

def import_data():
    with open('quotes.json', 'r', encoding='utf-8') as f:
        quotes = json.load(f)
        quotes_collection.insert_many(quotes)
    
    with open('authors.json', 'r', encoding='utf-8') as f:
        authors = json.load(f)
        authors_collection.insert_many(authors)

def main():
    import_data()
    print("Data imported successfully")

if __name__ == "__main__":
    main()
