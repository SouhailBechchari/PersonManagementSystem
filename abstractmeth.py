from abc import ABCMeta, abstractmethod

class Personne(metaclass=ABCMeta):
    X = 0
    def __init__(self, code, nom, prenom, age):
        Personne.X += 1
        self.code = code
        self.nom = nom
        self.prenom = prenom
        self.age = age

    @abstractmethod
    def Tostring(self):
        pass

    @abstractmethod
    def Equals(self, other):
        pass

class Employee(Personne):
    Y = 0
    def __init__(self, code, nom, prenom, age, grade):
        super().__init__(code, nom, prenom, age)
        Employee.Y += 1
        self.grade = grade

    def Tostring(self):
        return self.__dict__

    def Equals(self, other):
        return self.code == other.code

class Eleve(Personne):
    Z = 0
    def __init__(self, code, nom, prenom, age, level):
        super().__init__(code, nom, prenom, age)
        Eleve.Z += 1
        self.level = level

    def Tostring(self):
        return self.__dict__

    def Equals(self, other):
        return self.code == other.code

emp1 = Employee('red', 'dd', 'sali', 'jj', 'A')
emp2 = Employee('duc', 'dhd', 'zh', 'js', 'B')
emp3 = Employee('nn', 'qq', 's', 'dd', 'C')
elv1 = Eleve('ndsj', 'qjjsq', 's', 'dd', '10')

print(emp1.Tostring())
print(emp2.Equals(emp3))
print(emp3.Tostring())
print(elv1.Tostring())
print(Personne.X )
print(Employee.Y )
print(Eleve.Z)
