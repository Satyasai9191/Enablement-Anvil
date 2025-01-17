from ._anvil_designer import ManageUsersTemplate
from anvil import *
import anvil.server


class ManageUsers(ManageUsersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Admin.ManageUsers.ManageAdmin')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Admin.ManageUsers.ManageEmployee')
