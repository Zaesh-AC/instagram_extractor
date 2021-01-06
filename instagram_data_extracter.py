import json

def get_data():
    f = open('data/media.json')
    data = json.load(f)
    return data

def get_photos(data):
    return data.get('photos')

if __name__ == '__main__':
    data = get_data()
    photos = get_photos(data)
    for photo in photos:
        print(photo)