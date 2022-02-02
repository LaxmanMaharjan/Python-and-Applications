class Foo_or_Bar(type):
    # def __new__(cls, name, bases, attrs):
    #
    #     if 'foo' in attrs and 'bar' in attrs:
    #         raise TypeError(f"Class {name} can't contain both 'foo' and 'bar' attribures.")
    #
    #     if 'foo' not in attrs and 'bar' not in attrs:
    #         raise TypeError(f"Class {name} must either one of them.")
    #         #raise TypeError(f"Class {name} can't contain both 'foo' and 'bar' attributes.")
    #
    #     return super(Foo_or_Bar,cls).__new__(cls,name,bases,attrs)

    def __new__(cls, name, bases, attrs):
        answer = super(Foo_or_Bar,cls).__new__(cls, name, bases, attrs)
        if hasattr(answer,'foo') and hasattr(answer,'bar'):
            raise TypeError(f"Class {name} can't contain both 'foo' and 'bar'.")
        if not hasattr(answer,'foo') and not hasattr(answer,'bar'):
            raise TypeError(f"Class {name} must either 'foo' or 'bar'.")

        return answer

class valid(metaclass=Foo_or_Bar):
    foo = 'a'

# class invalid(metaclass=Foo_or_Bar):
#     pass

class also_valid(valid):
    pass


class KhowpaCollege(type):
    def __new__(cls, name, bases, attrs):
        if 'sanskar' not in attrs:
            raise TypeError(f"Class {name} must have sanskar")

        return super(KhowpaCollege,cls).__new__(cls,name, bases, attrs)
#
# class student(metaclass=KhowpaCollege):
#     # sanskar = "yes  i have sanskar"
#     pass

class student1:
    pass
def class_verification(Class): #alternate way to do so but in case of libray code and user code
    if not hasattr(Class,'sanskar'):
        raise TypeError(f"Class {Class.__name__} must have sanskar")

class_verification(student1)