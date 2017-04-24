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

artefacts = Artefact.objects.all()
art_name = [i.ObjectName for i in artefacts]

from collections import Counter
results = Counter(art_name).most_common(20)
most_common_objname = []
for arts in results:
    arts = list(arts)
    most_common_objname.append(arts[0])
    print(arts)
print(most_common_objname)

def delete_empty_objname():
    artefacts = Artefact.objects.all()
    for obj in artefacts:
        if obj.ObjectName == '':
            obj.delete()
            print('deleted')

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
                aa.append(a)
                print('a {0}'.format(a))
    elif ';' in i:
        i = i.split(';')
        aa.append(i)
    print(i)

#Top 4 Country and Others
art_country = [i.ManuCountry for i in artefacts]

#All color-1 color-2 (All Countries; Canada; (USA)

#group1
art_group = [i.group1 for i in artefacts]


#category1
art_category1 = [i.category1 for i in artefacts]

def materials(material):
    #print('original: {0}'.format(material))
    if len(material) == 0 :
        return None
    if '->' not in material or ';' not in material:
        #print('final --->{0}'.format(material))
        return material
    if '->' in material:
        material =  material.split('->')
        for a in  material:
            if ';' in a:
                a = a.split(';')
                aa.append(a)
    elif ';' in  material:
        material =  material.split(';')
        aa.append(material)
    #print(material)
    other_mat = []
    if len(material) == 1:
        return material
    for mat in material:
        if ';' in mat:
            mat = mat.replace(';', ' ')
            #print(mat)
            other_mat.append(mat.strip())
        else:
            other_mat.append(mat)
    #print(other_mat)
    material = ';'.join(other_mat)
    material = material.strip()
    #print(material)
    return material

artefacts = Artefact.objects.all()
for artefact in artefacts:
    if artefact.ObjectName == '':
        artefact.delete()
    else:
        material = materials(artefact.material)
        artefact.material = material
        artefact.save()
        print(material)


art_material = [i.material for i in artefacts]

'''
In [99]: materials('paper->;fibre->cotton')
a ['', 'fibre']
['paper', ';fibre', 'cotton']

In [100]: materials('glass;metal;paper;ceramic;synthetic')
['glass', 'metal', 'paper', 'ceramic', 'synthetic']

In [101]:
'''