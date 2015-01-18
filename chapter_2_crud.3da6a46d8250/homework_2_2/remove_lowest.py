import pymongo
from pymongo import MongoClient


# Connect to MongoDB database and set collection.
client = MongoClient('localhost', 27017)
db = client.students
collection = db.grades

# Query to locate all homework documents and sort by student_id and score.
query = {"type": "homework"}
selector = [("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)]


# Removes lowest homework document from each student_id.
def find_and_remove():
    dropped = {}
    for doc in collection.find(query).sort(selector):
        student = doc["student_id"]
        score = doc["score"]
        if student not in dropped:
            dropped[student] = score
            collection.remove(doc)


find_and_remove()
