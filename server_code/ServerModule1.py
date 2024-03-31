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


@anvil.server.callable
def merge_data(name=None, prn=None, address=None, email=None, mobile=None, blood=None,
               tenth=None, twelth=None, cet=None, jee=None, sem=None,
               certification=None, linkedin=None, experience=None):
    # Retrieve an existing row from the combine_data table (or create one if it doesn't exist)
    combine_data = app_tables.combine_data.get_or_create()
    
    # Update the row with data from the respective tables
    if name is not None:
        combine_data['name'] = name
    if prn is not None:
        combine_data['prn'] = prn
    if address is not None:
        combine_data['address'] = address
    if email is not None:
        combine_data['email'] = email
    if mobile is not None:
        combine_data['mobile'] = mobile
    if blood is not None:
        combine_data['blood'] = blood
    if tenth is not None:
        combine_data['tenth'] = tenth
    if twelth is not None:
        combine_data['twelth'] = twelth
    if cet is not None:
        combine_data['cet'] = cet
    if jee is not None:
        combine_data['jee'] = jee
    if sem is not None:
        combine_data['sem'] = sem
    if certification is not None:
        combine_data['certification'] = certification
    if linkedin is not None:
        combine_data['linkedin'] = linkedin
    if experience is not None:
        combine_data['experience'] = experience

    # Save the updated row
    combine_data.save()