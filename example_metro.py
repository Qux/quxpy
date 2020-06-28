from quxpy import metro

def foo():
    print("foo")

def bar():
    print("bar")

metro.add(foo, 1.0)  # name, func, interval in sec
metro.add(bar, 0.5)

try:
    metro.start()        
except KeyboardInterrupt:
    metro.terminate()
    
