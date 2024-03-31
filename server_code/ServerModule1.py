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
    # Add a new row to combine_data table
    personalinfo = app_tables.personalinfo.add_row()
  

@anvil.server.callable
def submit2(tenth, twelth, cet, jee, sem):
    # Add a new row to combine_data table
    academicinfo = app_tables.combine_data.add_row()
  
@anvil.server.callable
def submit3(certification, linkedin, experience):
    # Add a new row to combine_data table
    experienceinfo = app_tables.combine_data.add_row()
    

  combine_data.add_row('')
