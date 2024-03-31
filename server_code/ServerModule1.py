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


import anvil.server

@anvil.server.callable
def submit1(name, prn, address, email, mobile, blood):
    # Update the row in combine_data table
    combine_data = app_tables.combine_data.get_or_create()
    combine_data.update(name=name, prn=prn, address=address, email=email, mobile=mobile, blood=blood)

    # Update the row in personalinfo table
    personal_info = app_tables.personalinfo.get_or_create()
    personal_info.update(name=name, prn=prn, address=address, email=email, mobile=mobile, blood=blood)

@anvil.server.callable
def submit2(tenth, twelth, cet, jee, sem):
    # Update the row in combine_data table
    combine_data = app_tables.combine_data.get_or_create()
    combine_data.update(tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)

    # Update the row in academicinfo table
    academic_info = app_tables.academicinfo.get_or_create()
    academic_info.update(tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)

@anvil.server.callable
def submit3(certification, linkedin, experience):
    # Update the row in combine_data table
    combine_data = app_tables.combine_data.get_or_create()
    combine_data.update(certification=certification, linkedin=linkedin, experience=experience)

    # Update the row in experienceinfo table
    experience_info = app_tables.experienceinfo.get_or_create()
    experience_info.update(certification=certification, linkedin=linkedin, experience=experience)
