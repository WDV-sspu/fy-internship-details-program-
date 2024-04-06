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
    prn_input = self.text_box_2.text
    email = self.text_box_3.text
    mobile_input = self.text_box_4.text
    address = self.text_box_5.text
    blood = self.text_box_6.text

    try:
        prn = int(prn_input)
        if len(prn_input) != 10:
            alert("PRN must be exactly 10 digits")
            return  
    except ValueError:
        alert("Invalid PRN: Please enter a numeric value")
        return  

    try:
        mobile = int(mobile_input)
        if len(mobile_input) != 10:
            alert("Mobile number must be exactly 10 digits")
            return  
    except ValueError:
        alert("Invalid mobile number: Please enter a numeric value")
        return
      
    open_form('Form2')
anvil.server.call('submit1', name=name, prn=prn_input, address=address, email=email, mobile=mobile_input, blood=blood)
    