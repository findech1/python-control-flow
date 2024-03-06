#Switch Case implement in Python using Class
class Python_Switch:
	def day(self, month):

		default = "Incorrect day"

		return getattr(self, 'case_' + str(month), lambda: default)()

	def case_1(self):
		return "Jan"

	def case_2(self):
		return "Feb"

	def case_3(self):
		return "Mar"
my_switch = Python_Switch()

print(my_switch.day(1))
print(my_switch.day(2))
print(my_switch.day(3))

#Switch Case implement in Python using if-else
bike = 'Yamaha'

if bike == 'Hero':
	print("bike is Hero")

elif bike == "Suzuki":
	print("bike is Suzuki")

elif bike == "Yamaha":
	print("bike is Yamaha")

else:
	print("Please choose correct answer")
