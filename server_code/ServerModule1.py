import anvil.secrets
import anvil.server
from anvil.tables import app_tables
import hashlib
import binascii
import os


@anvil.server.callable
def check_unique_id(id_no):
  existing_user = app_tables.users.get(id_no=id_no)
  return existing_user is None


@anvil.server.callable
def submit(full_name,email_user,user_phonenumber,user_password,reenter_password):
  app_tables.users.add_row(full_name=full_name, email_user = email_user, user_phonenumber=  user_phonenumber,user_password = user_password,reenter_password = reenter_password, id_no,user_type="Admin")

# Insert the new admin details into the users table
  app_tables.users.add_row(
    full_name=full_name,
    email_user=email_user,
    user_phonenumber=user_phonenumber,
    user_password=user_password,
    id_no=id_no
  )