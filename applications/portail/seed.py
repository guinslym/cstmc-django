"""
with open('hello.json') as data:
	data = json.load(data)

aaa = list(data.keys())

for i in aaa:
	Artefact.objects.create(IDNO=i, **(data.get(i)))
"""

from applications.wadiyabi.models import Product, Comment
from applications.myprofile.models import UserProfile
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from faker import Factory
import random
from friendship.models import Friend, Follow


"""
def create_users():
    print('Create users and their profile')
    for i in range(10):
        user = mixer.blend(User)
        mixer.blend(UserProfile, user=user)

def create_comment(user, product):
    print('Create comment for user {0}'.format(user))
    if random.randint(0,1):
        comment = mixer.blend(Comment, author=user, product=product)

"""