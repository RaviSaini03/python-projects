class ravi:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
    
obj = ravi(12)
obj.ten_value = 120
print(obj.ten_value)
obj.show()