class PyCharm:
    def execute(self):
        print('Running..')
        print('Compiling')

class MyEidtor:
    def execute(self):
        print('Error Check')
        print('Convention Check')
        print('Running..')
        print('Compiling')


class Laptop:
    def code(self,ide):
        ide.execute()


ide1=PyCharm()
ide2=MyEidtor()



lap1=Laptop()
lap1.code(ide1)
print('________________________________')
lap2=Laptop()
lap2.code(ide2)
