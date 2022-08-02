def get_data(name):
    # from pymongo import MongoClient
    # import pymongo

    # CONNECTION_STRING = "mongodb+srv://localhost:27017/Coffee"

    # from pymongo import MongoClient
    # client = MongoClient(CONNECTION_STRING)

    # return client['user_shopping_list']
    
    from pymongo import MongoClient
    import pandas as pd

    client = MongoClient('localhost', 27017)
    db = client.Coffee
    collection = db.coffee
    data = pd.DataFrame(list(collection.find( {"Name" : name} )))
    return data


# if __name__ == "__main__":
#     data = get_data("Latte")
#     print(''.join(data["Content"].values))