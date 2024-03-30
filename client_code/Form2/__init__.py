from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    tenth = self.text_box_1.text
    twelth = self.text_box_2.text
    jee = self.text_box_3.text
    cet = self.text_box_4.text
    sem = self.text_box_5.text
    anvil.server.call('submit2', tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)
    open_form('Form3')
    
    
