data1 = ['WorkSpace', 'React', 'Angular', 'Veu', 'Private', 'Classified', 'Word File.doc']
data2 = ['workspace', 'react', 'angular', 'veu', 'private', 'classified', 'wordFile']

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ', '').lower()
assert data1 == data2
