from ._anvil_designer import Form2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form2(Form2Template):
    def __init__(self, **properties):
        # Any initialization code can go here, if needed
        pass

    def text_box_1_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in text_box_1"""
        pass

    def button_1_click(self, **event_args):
        tenth_input = float(self.text_box_1.text.rstrip('%'))
        twelth_input = float(self.text_box_2.text.rstrip('%'))
        jee_input =float(self.text_box_3.text.rstrip('%'))
        cet_input = float(self.text_box_4.text.rstrip('%'))
        sem_input = float(self.text_box_5.text.rstrip('%'))
        
        
        try:
            tenth = tenth_input
            if not 0 <= tenth <= 100:
                alert("Tenth percentage must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for tenth percentage")
            return

        try:
            twelth = twelth_input
            if not 0 <= twelth <= 100:
                alert("Twelth percentage must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for twelth percentage")
            return

        try:
            jee = jee_input  
            if jee is not None and not 0 <= jee <= 100:
                alert("JEE score must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for JEE score")
            return

        try:
            cet = cet_input 
            if cet is not None and not 0 <= cet <= 100:
                alert("CET score must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for CET score")
            return

        try:
            sem = sem_input 
            if sem is not None and not 0 <= sem <= 100:
                alert("SEM score must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for SEM score")
            return

        anvil.server.call('submit2', tenth=tenth_input, twelth=twelth_input, cet=cet_input, jee=jee_input, sem=sem_input)
        open_form('Form3')

       
