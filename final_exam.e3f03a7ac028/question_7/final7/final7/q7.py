import pymongo

# Connect to db and collection
connection = pymongo.Connection("mongodb://localhost", port=27017, safe=True)
db = connection.music
albums = db.albums
images = db.images

# Create images index
db.albums.ensure_index("images", 1)

# All images and albums
orphans = []
all_images = images.find()
all_albums = albums.find()

# Creates dictionary of all images that have an album
album_images = {}
for album in all_albums:
    for image in album['images']:
        if album_images.get(image):
            album_images[image] = album_images[image] + 1
        else:
            album_images[image] = 1

# Removes all images that do not have an album
for image in all_images:
    if image['_id'] not in album_images:
        orphans.append(image['_id'])
        images.remove({'_id': image['_id']})

# Total number of images that are tagged kittens
print images.find({'tags': 'kittens'}).count()
