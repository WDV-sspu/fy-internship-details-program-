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
    linkdin = self.text_box_1.text
    experience = self.text_box_2.text
    selected_options = [option for option in self.multiple_select_1.selected_values]

    media_file = anvil.media.upload()

    if media_file:
        media_url = media_file.get_url()
    else:
        media_url = None

    anvil.server.call('submit3', certification=certification, linkedin=linkedin, experience=experience, media_url=media_url, selected_options=selected_options)
