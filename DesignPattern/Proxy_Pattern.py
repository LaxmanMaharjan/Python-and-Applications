"""
Proxy is a structural design pattern that provides an object that acts as a substitute for a real service object
used by a client. A proxy receives client requests,
does some work (access control, caching, etc.) and then passes the request to a service object.
"""
from abc import ABC, abstractmethod

class Subject:
    """
    The Subject interface declares common operations for both ConcreteSubject and
    the Proxy. As long as the client works with ConcreteSubject using this
    interface, you'll be able to pass it a proxy instead of a  subject.
    """
    @abstractmethod
    def DoSomething(self):
        pass

class ConcreteSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """
    def DoSomething(self):
        print("Function of concrete subject is being called.")
        print("DoSomething() is being executed from concrete subject.")

class Proxy(Subject):
    """
    The Proxy has an interface identical to the ConcreteSubject.
    """
    concrete_obj = None
    def check_access(self):
        print("Checking access before calling the function of ConcreteSubject.")
        return True

    def DoSomething(self):
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """
        if self.check_access(): #example of controlling access to ConcreteSubject function
            Proxy.concrete_obj = ConcreteSubject()
            Proxy.concrete_obj.DoSomething()
print('*'*30)
print("Proxy Pattern Demo")
print('*'*30)
p = Proxy()
p.DoSomething()