class Persona():

    def __init__(self, fio, age, height, weight):
        self.fio = fio
        self.age = age
        self.height = height
        self.weight = weight


    def BMI(self): #расчет индекса массы тела
        return round((self.weight/(self.height * self.height)), 2)


    def __str__(self):
        return (f" {self.fio} {self.age} {self.height} {self.weight} {self.BMI()}")

    def __eq__(self, other):
        return (self.BMI() == other.BMI())

    def __lt__(self, other):
        return (self.BMI() < other.BMI())

    def __le__(self, other):
        return (self.BMI() <= other.BMI())

    def __repr__(self):
        return str(self.weight)





class MyList(list):

    def __str__(self):
        temp = ""
        for i in self:
            temp += i.__str__()
        return(temp)




list_pers = MyList()
user_file = open('person.data', 'r', encoding='utf8')
while True:
    item = user_file.readline()
    if item == '' or item == '\n':
        break
    temp_list = item.split(';')
    p = Persona(temp_list[0], int(temp_list[1]), float(temp_list[2]), int(temp_list[3]))
    list_pers.append(p)
user_file.close()

#p = Persona('Иван Иванович Иванов', 30, 1.75, 60)
print(list_pers)
print(list_pers[0].BMI())
print(list_pers[3] == list_pers[4])
list_pers.sort()
print(list_pers)