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
    # Check if a row already exists in the combine_data table
    rows = app_tables.combine_data.search()
    if rows:
        # Update the first row found
        combine_data = rows[0]
    else:
        # Create a new row if no row exists
        combine_data = app_tables.combine_data.add_row()
    
    # Update the row with the data from submit1
    combine_data.update(name=name, prn=prn, address=address, email=email, mobile=mobile, blood=blood)

@anvil.server.callable
def submit2(tenth, twelth, cet, jee, sem):
    # Check if a row already exists in the combine_data table
    rows = app_tables.combine_data.search()
    if rows:
        # Update the first row found
        combine_data = rows[0]
    else:
        # Create a new row if no row exists
        combine_data = app_tables.combine_data.add_row()
      
    # Update the row with the data from submit2
    combine_data.update(tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)

@anvil.server.callable
def submit3(certification, linkedin, experience):
    # Check if a row already exists in the combine_data table
    rows = app_tables.combine_data.search()
    if rows:
        # Update the first row found
        combine_data = rows[0]
    else:
        # Create a new row if no row exists
        combine_data = app_tables.combine_data.add_row()
    
    # Update the row with the data from submit3
    combine_data.update(certification=certification, linkedin=linkedin, experience=experience)
