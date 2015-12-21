class Girl:
    
    gender = 'female'
    
    def __init__(self, name):
        self.name = name

r = Girl('Rachel')
s = Girl('Stanky')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)