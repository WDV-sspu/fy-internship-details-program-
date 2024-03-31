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
    
    # Update the row with data from submit1
    personalinfo.update(name=name, prn=prn, address=address, email=email, mobile=mobile, blood=blood)


@anvil.server.callable
def submit2(tenth, twelth, cet, jee, sem):
    # Add a new row to combine_data table
    academicinfo = app_tables.academicinfo.add_row()
    
    # Update the row with data from submit2
    academicinfo.update(tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)

@anvil.server.callable
def submit3(certification, linkedin, experience):
    # Add a new row to combine_data table
    expericeneinfo = app_tables.expericeneinfo.add_row()
    
    # Update the row with data from submit3
    expericeneinfo.update(certification=certification, linkedin=linkedin, experience=experience)

@anvil.server.callable
def merge_data():
    # Retrieve data from personalinfo table
    personalinfo_rows = app_tables.personalinfo.search()
    # Retrieve data from academicinfo table
    academicinfo_rows = app_tables.academicinfo.search()
    # Retrieve data from expericeneinfo table
    expericeneinfo_rows = app_tables.expericeneinfo.search()

    print("Number of rows in academicinfo table:", len(academicinfo_rows))
    print("Contents of academicinfo table:", academicinfo_rows)

    # Create or get the single row from combine_data table
    if len(personalinfo_rows) == 1:
        personalinfo_row = personalinfo_rows[0]
        combine_data_row = app_tables.combine_data.get_or_create(name=personalinfo_row['name'], prn=personalinfo_row['prn'])
    else:
        return "No data found in personalinfo table!"

    # Update combine_data row with data from academicinfo table
    if len(academicinfo_rows) == 1:
        academicinfo_row = academicinfo_rows[0]
        combine_data_row.update(
            tenth=academicinfo_row['tenth'],
            twelth=academicinfo_row['twelth'],
            cet=academicinfo_row['cet'],
            jee=academicinfo_row['jee'],
            sem=academicinfo_row['sem']
        )
    else:
        return "Incorrect number of rows in academicinfo table!"

    # Update combine_data row with data from expericeneinfo table
    if len(expericeneinfo_rows) == 1:
        expericeneinfo_row = expericeneinfo_rows[0]
        combine_data_row.update(
            certification=expericeneinfo_row['certification'],
            linkedin=expericeneinfo_row['linkedin'],
            experience=expericeneinfo_row['experience']
        )
    else:
        return "Incorrect number of rows in expericeneinfo table!"

    return "Data merged successfully!"
