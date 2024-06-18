from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://mykytapohorelov:Goodwin7471@cluster0.5qnky6f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['cats_db']
collection = db['cats']

class MongoDBError(Exception):
    pass
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        raise MongoDBError(f"Error reading all cats: {e}")
def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Cat not found")
    except Exception as e:
        raise MongoDBError(f"Error reading cat by name: {e}")
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print("Cat's age updated")
        else:
            print("Cat not found")
    except Exception as e:
        raise MongoDBError(f"Error updating cat's age: {e}")
def add_feature_to_cat(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count > 0:
            print("Feature added to cat")
        else:
            print("Cat not found")
    except Exception as e:
        raise MongoDBError(f"Error adding feature to cat: {e}")
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Cat deleted")
        else:
            print("Cat not found")
    except Exception as e:
        raise MongoDBError(f"Error deleting cat by name: {e}")
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats")
    except Exception as e:
        raise MongoDBError(f"Error deleting all cats: {e}")
def main():
    try:
        cat = {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"]
        }
        collection.insert_one(cat)
        
        print("All cats:")
        read_all_cats()
        
        print("\nCat by name 'barsik':")
        read_cat_by_name("barsik")
        
        print("\nUpdating age of 'barsik' to 5:")
        update_cat_age("barsik", 5)
        read_cat_by_name("barsik")
    
        print("\nAdding new feature 'любить спати' to 'barsik':")
        add_feature_to_cat("barsik", "любить спати")
        read_cat_by_name("barsik")
    
        print("\nDeleting 'barsik':")
        delete_cat_by_name("barsik")
        read_all_cats()
        
        print("\nDeleting all cats:")
        delete_all_cats()
        read_all_cats()
        
    except MongoDBError as e:
        print(e)

if __name__ == "__main__":
    main()

def read_all_cats():

    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        raise MongoDBError(f"Error reading all cats: {e}")
