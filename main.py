# Importing the relevent libraries and packages
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import random

# Current Logged in user and variable for forgotten password restoration
global current_logged_user
global random_pass_name

# Synching with the kivi file
Builder.load_file('design.kv')

# Abstract class to avoid code duplication

class CommonMethods():
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

# Classes for the different pages of the app

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def forgot_password(self):
        self.manager.current = "forgot_password"

    def login(self, id, password):
        with open("users.json") as file:
            users = json.load(file)
        if (id in users) and (users[id]["user_password"] == password):
            global current_logged_user
            current_logged_user = id
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong id or password !"

class SignUpScreen(Screen, CommonMethods):
    # Adding user to json file database and documenting creation time
    def add_user(self, user_id, user_password):
        with open("users.json") as file:
            users = json.load(file)

        if (user_id in users) or (user_id == ""):
            self.ids.username_taken.text = "Please select a different user id"

        elif user_id == "" or user_password == "":
            self.ids.username_taken.text = "Please insert a valid user and password !"

        else:
            users[user_id] = {'user_id': user_id, 'user_password': user_password, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S"), 'passwords': dict()}

            with open("users.json", 'w') as file:
                json.dump(users, file)
                # Transfers user to update page on successful regestriation
                self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen, CommonMethods):
    pass

class ForgotPassword(Screen, CommonMethods):
    def generate_question(self, user_id):
        with open("users.json") as file:
            users = json.load(file)

        if (user_id not in users) or (user_id == ""):
            self.ids.restore_password_question.text = "Please check the submitted user name"

        elif (user_id in users):
            global current_logged_user
            global random_pass_name
            current_logged_user = user_id
            random_pass_name = random.choice(list(users[user_id]["passwords"]))
            self.ids.restore_password_question.text = "What is the password of " + random_pass_name + " ?"

    def answer_question(self, answer):
        global current_logged_user
        global random_pass_name

        with open("users.json") as file:
            users = json.load(file)

        if users[current_logged_user]["passwords"][random_pass_name] == answer:
            self.ids.restored_password.text = "Your password is: " + users[current_logged_user]["user_password"]
        else:
            self.ids.restored_password.text = "     Your password is wrong,\n you can try generating a new question"

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
            self.ids.required_password_output.text = passwords[current_logged_user]["passwords"][required_password]
        else:
            self.ids.required_password_output.text = "Wrong password name, please try again !"

    # Adds a new password to the database
    def add_password(self, new_password_name, new_password):

        if (new_password_name == "" or new_password == ""):
            self.ids.password_added.text = "Please insert a valid password !"

        else:
            with open("users.json") as file:
                passwords = json.load(file)

            passwords[current_logged_user]["passwords"][new_password_name] = new_password

            with open("users.json", 'w') as file:
                json.dump(passwords, file)

            self.ids.password_added.text = "New password added successfully"

class RootWidget(ScreenManager):
    pass

# Main
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
