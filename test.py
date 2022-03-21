
<LoginScreen>:
    canvas.before:
        Color:
            rgba: (36/255, 117/255, 173/255, 0.8)
        Rectangle:
            pos: self.pos
            size: self.size
    GridLayout:
        cols: 1
        GridLayout:
            cols: 1
            padding: 15, 15
            spacing: 10, 10
            Label:
                text: "Password Manager"
                font_size: '32sp'
                font_name: "Papyrus"
            RelativeLayout:
                TextInput:
                    id: user_id
                    hint_text: "User id"
                    size_hint: 0.7, 0.4
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    background_color: 1, 1, 1, 0
                    foreground_color: [1, 1, 1, 1]
                    hint_text_color: [1, 1, 1, 1]
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            points: self.x + 8, self.y, self.x + self.width, self.y
                            width: 1
            RelativeLayout:
                TextInput:
                    id: user_password
                    password: True
                    hint_text: "User Password"
                    size_hint: 0.7, 0.4
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    background_color: 1, 1, 1, 0
                    foreground_color: [1, 1, 1, 1]
                    hint_text_color: [1, 1, 1, 1]
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            points: self.x + 8, self.y, self.x + self.width, self.y
                            width: 1
            Label:
                id: login_wrong
                text: ""
            RelativeLayout:
                Button:
                    text: "Login"
                    color: 36/255, 117/255, 173/255, 0.8
                    bold: True
                    size_hint: 0.3, 0.5
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    on_press: root.login(root.ids.user_id.text, root.ids.user_password.text)
                    opacity: 1 if self.state == 'normal' else 0.5
                    background_normal: ''
                    background_color: 255/255, 215/255, 0, 0.8
