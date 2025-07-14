def greets(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thanks for Visiting!!")
    return mfx

@greets
def hello():
    print("Hello! My name is Ravi Saini.")

def mul(a,b):
    print(a*b)

hello()
greets(mul)(3,4)