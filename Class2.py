class A:
    def say_hello(self):
        print("Hello")


class B(A):
    def say_goodbye(self):
        print("Goodbye")

b = B()
b.say_hello()
b.say_goodbye()
