class Phone:
    "A simple class for test"
    version_name="7"
    brand_name="One Plus"
    user_name=""

    model="Plus"
    def get_model(self):
        return self.model
        #return "Plus"

    def set_model(self,val):
        self.model="Plus, "+ val
    #constructor
    def __init__(self,user):
        self.user_name=user

    def BootLogo(self):
        print("One Plus",self.version_name)

#create object
prabhat = Phone("Prabhat phone")
#prabhat.version_name = 12
#print(prabhat.model)
prabhat.BootLogo()
print(prabhat.get_model())
prabhat.set_model("NEW")
print(prabhat.get_model())