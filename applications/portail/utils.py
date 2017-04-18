from random import randint

def get_background_image():
    image = [
                'camera-1149767_1280.jpg',
                'camera-711025_1280.jpg',
                'clock-tower-190677_1280.jpg',
                'car-2072471_1280.jpg',
            ]
    return 'img/'+image[randint(0,3)]

def language_set(language):
    if "-" in language:
        return (language.split('-')[1]).upper()
    else:
        return language.upper()