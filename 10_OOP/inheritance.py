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
class Phone:
    IMEI = None
    producer = "IT DEPT"

    def call_by_4g(self):
        print("4g call is on")

class NFCReader:
    nfc_type = "5th generation"
    producer = "HM"

    def read_card(self):
        print("NFC reading card")

    def write_card(self):
        print("NFC writing card")

class RemoteControl:
    rc_type = "Infrared Remote Control "

    def control(self):
        print("Infrared Remote Control is on")

class Phone2024(Phone, NFCReader, RemoteControl):
    pass  # "pass" is to tell Python, “I'm not adding any code here for now, but this class must exist and remain legal

phone = Phone2024()
print("The producer is: " + phone.producer)
phone.call_by_4g()
phone.read_card()
phone.read_card()
phone.control()