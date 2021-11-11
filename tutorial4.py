class UseDebugger:
    def calculations(self, a, b):
        print("in calculations")
        a = 3 + 5
        b = 1

        if a > b:
           # raise TypeError(" theres been an error")
           # print(a, "is smaller then", b)
            a/b
        else:
            print(a, "is smaller than ", b)


debug_me = UseDebugger()
debug_me.calculations(8, 0)
try :
    debug_me.calculations(8,0)
except TypeError as te:
    print(te)
except Exception as e:
    print(e)
else:
    print("all good")
finally:
    print("graceful end no matter what")


