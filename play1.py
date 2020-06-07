
class Ordnungsamt:
    def __init__(self,mann):
        self.mann = mann
        self.mann.set_name('Anton')

    
class Mann:
    def __init__(self):
        self.name = None
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name

mann = Mann()


mann.set_name('Stefan') 
print(mann.get_name())

dummy = Ordnungsamt(mann)
print(mann.get_name())




