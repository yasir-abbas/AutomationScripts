#This is api for Have i been pawned


import pyhibp
from pyhibp import pwnedpasswords as pw



pyhibp.set_user_agent(ua="Awesome application/0.0.1 Using this for research purpose")

resp = pw.is_password_breached(password="secret123")
print(resp)



# Get data classes in the HIBP system
resp = pyhibp.get_data_classes()



# Get all breach information
resp = pyhibp.get_all_breaches()
print(resp[0])
# Get a single breach
resp = pyhibp.get_single_breach(breach_name="Adobe")

print(resp)


# This part is paid to use
# An API key is required for calls which search by email address
#   (so get_pastes/get_account_breaches)
# See <https://haveibeenpwned.com/API/Key>
HIBP_API_KEY = None

if HIBP_API_KEY:
    # Set the API key prior to using the functions which require it.
    pyhibp.set_api_key(key=HIBP_API_KEY)

    # Get pastes affecting a given email address
    resp = pyhibp.get_pastes(email_address="test@example.com")

    # Get breaches that affect a given account
    resp = pyhibp.get_account_breaches(account="test@example.com", truncate_response=True)


