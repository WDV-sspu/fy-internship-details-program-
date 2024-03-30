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

  
def button_1_click(self, **event_args):
    try:
        # Get the input values from the components
        certificate = self.text_box_1.text
        linkedin = self.text_box_2.text
        experience = self.text_box_3.text
        anvil.server.call('submit3', certification=certificate, linkedin=linkedin, experience=experience)
        open_form('Form4')

    except Exception as e:
        # Handle other exceptions
        alert(f"An error occurred: {e}")