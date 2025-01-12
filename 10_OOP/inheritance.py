# single inheritance
# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class
class Child(Parent):
	def func2(self):
		print("This function is in child class.")

object = Child()
object.func1()
object.func2()


# Multiple Inheritance
# Base class1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)
# Base class2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father:", self.fathername)
        print("Father:", self.mothername)

s1 = Son()
s1.fathername = "Tom"
s1.mothername = "Olivia"
s1.parents()
