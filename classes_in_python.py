class Dog():
	"""A simple attempt to model a dog"""


	#Python runs __init__ whenever a new object is instantiated
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age
		print("Dog initialization is complete")


	def sit(self):
		print(self.name.title() + " is now sitting.")


	def roll_over(self):
		print(self.name.title() + " rolled over.")

#Inheritance:
class GermanShepherd(Dog):
	def __init__(self, name, age):
		super().__init__(name, age)
		print("Ein Hund wurde geboren")

	#overriding a parent method	
	def sit(self):
		super().sit()
		print(".. in the chair")	

	def talk(self):
		print(self.name.title() + " says: Gutten Tag!")		

				

my_dog = Dog('Rex', 6)
my_dog.sit()
my_dog.roll_over()


smart_dog = GermanShepherd('Fritz', 20)
smart_dog.sit()
smart_dog.talk()


#Python allows to add attributes to object Dynamically
my_dog.color = 'red'
print(my_dog.color)

