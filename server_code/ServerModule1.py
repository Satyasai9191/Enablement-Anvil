import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def store_user_input(user_name, email, password):
#     app_tables.add_row(Email=email, Name=user_name, Password=password)

import anvil.tables as tables
from anvil.tables import app_tables
import bcrypt

# @anvil.server.callable
# def get_admin_users():
#     return app_tables.admin.search(usertype='admin')

@anvil.server.callable
def submit(full_name,email_user,user_phonenumber,user_password,reenter_password):
  app_tables.users.add_row(full_name=full_name, email_user = email_user, user_phonenumber=  user_phonenumber,user_password = user_password,reenter_password = reenter_password, user_type="Admin")
  # Hash the password before storing it
  hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
    
    # Store the hashed password in the data table
  anvil.server.get_app_tables().admin.add_row(
        full_name=full_name,
        email=email_user,
        phone_number=user_phonenumber,
        password=hashed_password
    )