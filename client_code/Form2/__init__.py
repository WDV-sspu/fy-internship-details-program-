from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2:
    def __init__(self, **properties):
        # Any initialization code can go here, if needed
        pass

    def text_box_1_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in text_box_1"""
        pass

    def button_1_click(self, **event_args):
        tenth_input = self.text_box_1.text
        twelth_input = self.text_box_2.text
        jee_input = self.text_box_3.text
        cet_input = self.text_box_4.text
        sem_input = self.text_box_5.text
        
        try:
            tenth = float(tenth_input.rstrip('%'))  
            if not 0 <= tenth <= 100:
                alert("Tenth percentage must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for tenth percentage")
            return

        try:
            twelth = float(twelth_input.rstrip('%'))  
            if not 0 <= twelth <= 100:
                alert("Twelth percentage must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for twelth percentage")
            return

        try:
            jee = float(jee_input.rstrip('%')) if jee_input.strip() else None 
            if jee is not None and not 0 <= jee <= 100:
                alert("JEE score must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for JEE score")
            return

        try:
            cet = float(cet_input.rstrip('%')) if cet_input.strip() else None 
            if cet is not None and not 0 <= cet <= 100:
                alert("CET score must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for CET score")
            return

        try:
            sem = float(sem_input.rstrip('%')) if sem_input.strip() else None 
            if sem is not None and not 0 <= sem <= 100:
                alert("SEM score must be between 0 and 100")
                return
        except ValueError:
            alert("Invalid input for SEM score")
            return

        anvil.server.call('submit2', tenth=tenth, twelth=twelth, cet=cet, jee=jee, sem=sem)
        open_form('Form3')
