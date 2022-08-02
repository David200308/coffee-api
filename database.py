from numpy import true_divide


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
    if (collection.count_documents( { "Name": name} ) != 0):
        data = pd.DataFrame(list(collection.find( {"Name" : name} )))
        content_list = data["Content"].values
        for x in content_list:
            content = x
        return content
    else:
        return "null"


# if __name__ == "__main__":
#     data = get_data("srr")
#     print(data)
#     if bool(data == "null"):
#         content = "null"
#     else:
#         content = data

#     print(content)