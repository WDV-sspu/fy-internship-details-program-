from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        # Define and retrieve data variables
        name = self.text_box_1.text
        prn_input = self.text_box_2.text
        email = self.text_box_3.text
        mobile_input = self.text_box_4.text
        address = self.text_box_5.text
        blood = self.text_box_6.text
        tenth_input = self.text_box_7.text
        twelth_input = self.text_box_8.text
        jee_input = self.text_box_9.text
        cet_input = self.text_box_10.text
        sem_input = self.text_box_11.text
        experience = self.text_box_12.text
        linkedin = self.text_box_13.text
        work_experience = self.text_box_14.text

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

        # Call the server function and pass the data
        anvil.server.call('submit1',name=name,prn=prn,email=email,mobile=mobile,address=address,blood=blood,tenth=tenth,twelth=twelth,jee=jee,cet=cet,sem=sem,experience=experience,linkedin=linkedin,work_experience=work_experience)

        open_form('thankyou')
