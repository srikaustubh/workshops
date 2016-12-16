__author__ = 'jc449799'
x,y = 5.5,"jay"
try:
    result =  x*y
    print(result)
except ValueError:
    print("value")
except TypeError:
    print("type")
except:
    print("other")
