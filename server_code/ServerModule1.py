import anvil.secrets
import anvil.server
from anvil.tables import app_tables
import hashlib
import binascii
import os
@anvil.server.callable
def submit(full_name,email_user,user_phonenumber,user_password,reenter_password):
  app_tables.users.add_row(full_name=full_name, email_user = email_user, user_phonenumber=  user_phonenumber,user_password = user_password,reenter_password = reenter_password, user_type="Admin")

