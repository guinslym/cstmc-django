"""
with open('hello.json') as data:
	data = json.load(data)

aaa = list(data.keys())

for i in aaa:
	Artefact.objects.create(IDNO=i, **(data.get(i)))
"""

from applications.portail.models import Artefact
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from faker import Factory
import random

for i in range(200):
	artefact = mixer.blend(Artefact)


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

artefacts = Artefact.objects.all()
for art in artefacts:
    if len(art.image) < 10:
        art.delete()
    elif len(art.ObjectName) =='':
        art.delete()

#Javascript changing name (5)
art_name = [i.ObjectName for i in artefacts]

from collections import Counter
Counter(art_name)

a = Artefact.objects.first()
a._meta.get_all_field_names()

#delete all unknown name

artefacts = Artefact.objects.all()

#List of materials
art_material = [i.material for i in artefacts]
aa=[]
for i in art_material:
    if '->' in i:
        i = i.split('->')
        for a in i:
            if ';' in a:
                a = a.split(';')
                print('a {0}'.format(a))
    elif ';' in i:
        i = i.split(';')
    print(i)

#Top 4 Country and Others
art_country = [i.ManuCountry for i in artefacts]

#All color-1 color-2 (All Countries; Canada; (USA)

#group1
art_group = [i.group1 for i in artefacts]


#category1
art_category1 = [i.category1 for i in artefacts]