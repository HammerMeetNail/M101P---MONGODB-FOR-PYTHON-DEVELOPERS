from pymongo import MongoClient


# Connect to MongoDB database and set collection.
client = MongoClient('localhost', 27017)
db = client.school
collection = db.students

# Query to locate all homework documents and sort by student_id and score.
query = {"scores.type": "homework"}
selector = {"scores.type": 1, "scores.score": 1, "_id": 1}


# Locates all homework from a student
def find_homework():
    results = {}
    for doc in collection.find(query, selector):
        for score in doc['scores']:
                if score['type'] == 'homework':
                        if doc['_id'] in results:
                                results[doc['_id']].append(score['score'])
                        else:
                                results[doc['_id']] = [score['score']]
    return results


# Locates lowest homework document from each student.
def find_lowest():
    new_results = find_homework()
    for student in new_results:
        new_results[student].sort()
        new_results[student] = new_results[student][0]
    return new_results


# Removes lowest homework from each student
def remove_lowest():
    results = find_lowest()
    for student in results:
        new_query = {'_id': student}
        score = results[student]
        collection.update(new_query, {"$pull": {'scores': {'type': 'homework', 'score': score}}})


if __name__ == '__main__':
    remove_lowest()