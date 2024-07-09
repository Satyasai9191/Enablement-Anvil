from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    employee_users = list(app_tables.users.search())
    for user in employee_users:
        # print(f"User {user['user_type']} logged in.")
        if user['user_type'] == "admin":
          open_form('Admin')
        elif user['user_type']== "employee":
          open_form('Employee')
        else:
          alert('invalid user')
