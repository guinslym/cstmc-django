with open('hello.json') as data:
	data = json.load(data)

aaa = list(data.keys())

for i in aaa:
	Artefact.objects.create(IDNO=i, **(data.get(i)))