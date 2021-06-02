import buffer
import json
import sys

def collection_to_dict(filename):
    collections = {};
    with open(filename, "rb") as db:
        collections["version"] = buffer.read_uint(db)
        collections["num_collections"] = buffer.read_uint(db)
        collections["collections"] = []
        for i in range(collections["num_collections"]):
            collection = {}
            collection["name"] = buffer.read_string(db)
            collection["size"] = buffer.read_uint(db)
            collection["hashes"] = []
            for i in range(collection["size"]):
                collection["hashes"].append(buffer.read_string(db))
            collections["collections"].append(collection)
    return collections


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid args: read_collection.py <collection.db>")
    else:
        
        print(json.dumps(collection_to_dict(sys.argv[1]), indent=2))

