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

# Python code in Anvil Form

from anvil import *

class MyForm(MyFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        try:
            # Upload the selected file
            media_file = anvil.media.upload(file)

            # Get the URL of the uploaded file
            media_url = media_file.get_url()

            # Pass the URL to the server function
            anvil.server.call('submit3', certification=media_url)

        except Exception as e:
            # Handle any errors
            alert(f"An error occurred: {e}")

    def button_1_click(self, **event_args):
        try:
            # Get the input values from the components
            certificate = self.text_box_1.text
            linkedin = self.text_box_2.text
            experience = self.text_box_3.text

            # Call the server function with the input values
            anvil.server.call('submit3', certification=certificate, linkedin=linkedin, experience=experience)

            # Open Form4
            open_form('Form4')

        except Exception as e:
            # Handle other exceptions
            alert(f"An error occurred: {e}")
