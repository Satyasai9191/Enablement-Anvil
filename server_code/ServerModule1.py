import anvil.server
from anvil.tables import app_tables
import hashlib
import binascii
import os
@anvil.server.callable
def submit(full_name,email_user,user_phonenumber,user_password,reenter_password):
  app_tables.users.add_row(full_name=full_name, email_user = email_user, user_phonenumber=  user_phonenumber,user_password = user_password,reenter_password = reenter_password, user_type="Admin")

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

@anvil.server.callable
def submit_user(full_name, email_user, user_phonenumber, user_password):
    # Encrypt the password
    hashed_password = hash_password(user_password)
    
    # Store the data in the database
    app_tables.users.add_row(
        full_name=full_name,
        email_user=email_user,
        user_phonenumber=user_phonenumber,
        user_password=hashed_password
    )

@anvil.server.callable
def get_users():
    rows = app_tables.users.search()
    users = []
    for row in rows:
        # For display purposes, we will not decrypt the password but show a fixed string of dots
        users.append({
            'full_name': row['full_name'],
            'email_user': row['email_user'],
            'user_phonenumber': row['user_phonenumber'],
            'user_password': '•' * 8  # Display 8 dots for the password
        })
    return users