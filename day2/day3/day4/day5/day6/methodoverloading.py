class demo:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,*numbers):
        print(sum(numbers))

#main
obj=demo()
obj.add(8.9,9,0)
obj.add(10)
obj(10,20)