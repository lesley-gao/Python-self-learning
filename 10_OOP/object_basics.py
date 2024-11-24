# Example 1
class Student:
    name = None
    nationality = None
    city = None

    def sayhi(self):
        print(f"Hello World. My name is {self.name}")

    def say_hi2(self,msg):
        print(f"Hello everyone, {msg}. I come from {self.nationality} and lives in {self.city}.")

stu_1 = Student()

stu_1.name = "Michael"
stu_1.nationality = "New Zealand"
stu_1.city = "Auckland"

stu_1.sayhi()
stu_1.say_hi2("nice to meet you")


# Example 2
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID: {clock1.id}, 价格: {clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"闹钟ID: {clock2.id}, 价格: {clock2.price}")
clock2.ring()
