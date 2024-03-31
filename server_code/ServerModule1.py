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
    combine_data = app_tables.personalinfo.get_or_create(name=name, prn=prn, address=address, email=email, mobile=mobile, blood=blood)

@anvil.server.callable
def submit2(tenth, twelth, cet, jee, sem):
    combine_data = app_tables.academicinfo.get_or_create(tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)

@anvil.server.callable
def submit3(certification, linkedin, experience):
    combine_data = app_tables.expericeneinfo.get_or_create(certification=certification, linkedin=linkedin, experience=experience)
