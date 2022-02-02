"""
This example demonstrate about function Registry using Decorator
"""
registry = []
def register(fxn):
    registry.append(fxn)
    return fxn

@register
def foo():
    return 'foo'

@register
def bar():
    return 'bar'

ans = []
for fxn in registry:
    ans.append(fxn())
print(ans)