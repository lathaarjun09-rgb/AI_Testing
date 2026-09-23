import json
from datetime import datetime
from pathlib import Path

USER_FILE = Path("data/userdetails.json")

def generate_dynamic_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    return f"testuser{timestamp}@gmail.com"

def save_user_data(firstname,lastname,email,password):
    
    user_data = {"firstname": firstname,
                 "lastname":lastname,
                 "email": email,
                 "password":password,
                 "confirm_password":password}
    
    USER_FILE.parent.mkdir(parents = True,
                           exist_ok = True)
    
    with open(USER_FILE, "w") as file:
        json.dump(user_data , file, indent = 4)
        
def read_user_data():
    with open(USER_FILE,"r") as file:
        return json.load(file)        