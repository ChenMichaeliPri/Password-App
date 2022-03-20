# Importing the relevent libraries and packages
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

# Synching with the kivi file
Builder.load_file('design.kv')

# Classes for the different pages of the app
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class SignUpScreen(Screen):
    # Adding user to json file database and documenting creation time
    def add_user(self, userPassword):
        with open("users.json") as file:
            users = json.load(file)

        users["User: "+str(len(users)+1)] = {'userPassword': userPassword, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
            # Transfers user to update page on successful regestriation
            self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"

class RootWidget(ScreenManager):
    pass

# Main
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
