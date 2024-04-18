import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def submit1(name, prn, email, mobile, address, blood, tenth, twelth, jee, cet, sem, experience, linkedin, work_experience):
    app_tables.all_for_one.add_row(
        name=name,
        prn=prn,
        email=email,
        mobile=mobile,
        address=address,
        blood=blood,
        tenth=tenth,
        twelth=twelth,
        jee=jee,
        cet=cet,
        sem=sem,
        experience=experience,
        linkedin=linkedin,
        work_experience=work_experience
    )
    anvil.email.send(from_name = "My App Support", 
                 to = "email",
                 subject = "Welcome",
                 text = "Welcome to My App!")