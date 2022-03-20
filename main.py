# Importing the relevent libraries and packages
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

# Current Logged in user
current_logged_user = None

# Synching with the kivi file
Builder.load_file('design.kv')

# Classes for the different pages of the app

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, id, password):
        with open("users.json") as file:
            users = json.load(file)
        if (id in users) and (users[id]["user_password"] == password):
            current_logged_user = id
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong id or password !"

class SignUpScreen(Screen):
    # Adding user to json file database and documenting creation time
    def add_user(self, user_id, user_password):
        with open("users.json") as file:
            users = json.load(file)

        if user_id in users:
            self.ids.username_taken.text = "Please select a different user id"
        else:
            users[user_id] = {'user_id': user_id, 'user_password': user_password, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S"), 'passwords': dict()}

            with open("users.json", 'w') as file:
                json.dump(users, file)
                # Transfers user to update page on successful regestriation
                self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        current_logged_user = None
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    # Returns the required password from the database
    def extract_password(self, required_password):
        with open("users.json") as file:
            passwords = json.load(file)

        if required_password in passwords[current_logged_user]["passwords"]:
            required_password_output = passwords[current_logged_user]["passwords"][required_password]
        else:
            required_password_output = "Wrong password name, please try again !"

    # Adds a new password to the database
    def add_password(self, new_password_name, new_password):
        with open("users.json") as file:
            passwords = json.load(file)

        passwords[current_logged_user]["passwords"][new_password_name] = new_password

        with open("users.json", 'w') as file:
            json.dump(users, file)

        required_password_output = "New password added successfully"

class RootWidget(ScreenManager):
    pass

# Main
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
