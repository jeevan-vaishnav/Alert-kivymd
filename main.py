from tkinter import Button, dialog
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class AlertDialog(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('main.kv')

    def show_alert_button(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Hi Shreya , You are Cool now ?",
                text="This is Something ",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text="Yes iam Cool!",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.neetBtn
                    ),

                ],

            )
        self.dialog.open()
    # Click cancel Button

    def close_dialog(self, obj):
        # thats close the box
        self.dialog.dismiss()
    # click the need button

    def neetBtn(self, obj):
        # close the box
        self.dialog.dismiss()
        # Change the label

        self.root.ids.my_label.text = "Yeha Shreya is Cool Finally!!"


        # main start
AlertDialog().run()
