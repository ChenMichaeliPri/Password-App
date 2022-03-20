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
    def add_user(self, userPassword):
        with open("users.json") as file:
            users = json.load(file)

        users[userPassword] = {'userPassword': userPassword, 'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)

class RootWidget(ScreenManager):
    pass

# Main
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
