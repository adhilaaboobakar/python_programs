# tuple
# defined by ()
# insertion order preserved
# duplicates allowed
# immutable
# methods count(),index()

color=("red",)
print(type(color))

# one element alone can't become tuple. lf it wants that put a comma

tp=(10,50,20,30,10,"hello")
print(tp)
# tp[0]=100
print(tp.count(10))
print(tp.index(20))
