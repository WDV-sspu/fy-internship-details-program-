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
def submit1(name, prn, address, email, mobile, blood):
    app_tables.personalinfo.add_row(name=name, prn=prn, email=email, mobile=mobile, address=address, blood=blood)

def submit2(tenth, twelth, cet, jee, sem):
    app_tables.academicinfo.add_row(tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)


def submit3(certification, linkedin, experience):
    app_tables.expericenceinfo.add_row(certification=certification, linkedin=linkedin, experience=experience)
