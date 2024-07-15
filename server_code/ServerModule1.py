import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables




@anvil.server.callable
def submit(full_name, email_user, user_phonenumber, user_password, reenter_password):
  
    encrypted_password = anvil.secrets.encrypt_with_key('secret_key', user_password)
    encrypted_reenter_password = anvil.secrets.encrypt_with_key('secret_key', reenter_password)
  
    app_tables.users.add_row(
        full_name=full_name,
        email_user=email_user,
        user_phonenumber=user_phonenumber,
        user_password=encrypted_password,
        reenter_password=encrypted_reenter_password,
        user_type='admin'
    )
