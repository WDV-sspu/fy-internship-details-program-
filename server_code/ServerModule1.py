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
  combine_data_row = app_tables.combine_data.add_row(
    name=name,
    prn=prn,
    address=address,
    email=email,
    mobile=mobile,
    blood=blood
  )
  return combine_data_row

@anvil.server.callable
def submit2(tenth, twelth, cet, jee, sem):
    # Get the existing row from combine_data table
    combine_data_id = app_tables.combine_data.get_by_id()
    # Update the row with data from submit2
    combine_data_row.update(
        tenth=tenth,
        twelth=twelth,
        cet=cet,
        jee=jee,
        sem=sem
    )

@anvil.server.callable
def submit3(certification, linkedin, experience, row_id):
  # Get the existing row from combine_data table
  combine_data_row = app_tables.combine_data

  # Update the row with data from submit3
  combine_data_row.update(
    certification=certification,
    linkedin=linkedin,
    experience=experience
  )