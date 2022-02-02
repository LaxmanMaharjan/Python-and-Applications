"""
The method named __call__ is called when the instance is called as function

"""
class nepa:
    def __call__(self, *args, **kwargs):
        print("hello world!")

N = nepa()
N()