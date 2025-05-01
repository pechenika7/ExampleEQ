class Persona():

    def __init__(self, fio, age, height, weight, f = None):
        self.fio = fio
        self.age = age
        self.height = height
        self.weight = weight
        self.f = f

    def __str__(self):
        return (f" {self.fio} {self.age} {self.height} {self.weight} {self.f(self.weight, self.height)}")

    def __eq__(self, other):
        return (self.f(self.weight, self.height) == other.f(self.weight, self.height))

    def __lt__(self, other):
        return (self.f(self.weight, self.height) < other.f(self.weight, self.height))

    def __le__(self, other):
        return (self.f(self.weight, self.height) <= other.f(self.weight, self.height))

    def __repr__(self):
        return str(self.weight)





class MyList(list):

    def __str__(self):
        temp = ""
        for i in self:
            temp += i.__str__()
        return(temp)



def CalcID(x, y):
    return x

list_pers = MyList()
user_file = open('person.data', 'r', encoding='utf8')
while True:
    item = user_file.readline()
    if item == '' or item == '\n':
        break
    temp_list = item.split(';')
    p = Persona(temp_list[0], int(temp_list[1]), float(temp_list[2]), int(temp_list[3]), CalcID)
    list_pers.append(p)
user_file.close()

#p = Persona('Иван Иванович Иванов', 30, 1.75, 60)
print(list_pers)
print(list_pers[0].f(list_pers[0].weight, list_pers[0].height))
print(list_pers[3] == list_pers[4])
list_pers.sort()
print(list_pers)