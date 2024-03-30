from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    name = self.text_box_1.text
    prn = int(self.text_box_2.text)
    email = self.text_box_3.text
    mobile = int(self.text_box_4.text)
    address = self.text_box_5.text
    blood = self.text_box_6.text
    anvil.server.call('submit1',name=name,prn=prn,address=address,email=email,mobile=mobile,blood=blood)
    open_form('Form2')
    
  
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
