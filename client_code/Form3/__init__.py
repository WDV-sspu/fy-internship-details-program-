from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  
Sujhal Gurav <sujhal05gurav@gmail.com>
11:50 PM (0 minutes ago)
to me

def button_1_click(self, **event_args):
    try:
        # Get the input values from the components
        certificate = self.text_box_1.text
        linkedin = self.text_box_2.text
        experience = self.text_box_3.text

        # Handle multiple select component
        try:
            selected_options = [option for option in self.my_multiple_select.selected_values]
        except AttributeError:
            selected_options = []  # If the multiple select component is not present or selected_values is not available

        # Call the server function with all the input values
        anvil.server.call('submit3', certification=certificate, linkedin=linkedin, experience=experience, selected_options=selected_options)

    except Exception as e:
        # Handle other exceptions
        alert(f"An error occurred: {e}")