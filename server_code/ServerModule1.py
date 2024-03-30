import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
@anvil.server.callable
def submit1(self,name,prn,address,email,mobile,blood):
   self.name=name
   self.prn=prn
   self.address=address
   self.email=email
   self.mobile=mobile if not mobile.isdigit() or len(mobile) != 10:
        raise ValueError("Mobile number must be a 10-digit numeric value.")
   self.blood=blood

def submit2(self,tenth,twelth,cet,jee,sem,):
   self.tenth=tenth
   self.twelth=twelth
   self.cet=cet
   self.jee=jee
   self.sem=sem

def submit3(self,certification,linkdin,experience):
   self.certification=certification
   self.linkdin=linkdin
   self.experience=experience

anvil.email.send(from_name = "My App Support", 
                 to = email,
                 subject = "Welcome",
                 text = "Welcome to My App!")

def val_mobile(self):
  
   