"""
In this context, the term meta-coding refers to code that
inspects other code in the application.

"""
class Logged(type):
    """A metaclass that causes classes that it creates to log
    their function calls.
    """
    def __new__(cls, name, bases, attrs):
        for key,value in attrs.items():
            if callable(value):
                attrs[key] = cls.log_call(value)
        return super(Logged,cls).__new__(cls, name, bases, attrs)

    @staticmethod
    def log_call(fxn):
        """
        Given a function, wrap it with some logging code and
        return the wrapped function.
        """
        def inner(*args,**kwargs):
            print('The function %s was called with positional arguments %r and '
                    'keyword arguments %r.' % (fxn.__name__, args, kwargs))
            try:
                response = fxn(*args, **kwargs)
                print("The function %s was successful"%fxn.__name__)
                return response
            except Exception as exc:
                print(f"The fucntion call to {fxn.__name__} raised an exception: {exc} ")
                raise
        return inner
