import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
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
def submit1(name, prn, email, mobile, address, blood):
    # Here you can process the submitted data, save it to a database, or perform any server-side operations
    # For example, you can save the data to a table in Anvil's Data Tables
    app_tables.personal.add_row(name=name, prn=prn, email=email, mobile=mobile, address=address, blood=blood)
    app_tables.all_for_one.add_row(name=name, prn=prn, email=email, mobile=mobile, address=address, blood=blood)


@anvil.server.callable
def submit2(tenth,twelth,jee,cet,sem):
    app_tables.acedemic.add_row(tenth=tenth,twelth=twelth,jee=jee,cet=cet,sem=sem)
    app_tables.all_for_one.add_row(tenth=tenth,twelth=twelth,jee=jee,cet=cet,sem=sem)


@anvil.server.callable
def submit3(certifications,linkdin,experience):
    app_tables.experience.add_row(certifications=certifications,linkdin=linkdin,experience=experience)
    app_tables.all_for_one.add_row(certifications=certifications,linkdin=linkdin,experience=experience)
    q. all_of()