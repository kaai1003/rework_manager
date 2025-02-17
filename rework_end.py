import customtkinter
import os
from tkinter import messagebox
from PIL import Image
from datetime import datetime

from models.engine.database_manager import get_all
from models.engine.database_manager import get_obj
from models.reworkdetails import ReworkDetails
from models.engine.print_label import generate_label


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("START REWORK STATION")
        self.geometry("1050x800")
        self.operator = ""
        self.list_users = []

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "rework_icon.png")), size=(50, 50))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Rework-OUT.png")), size=(500, 170))
        self.large_login_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Reworkstart.png")), size=(500, 150))
        self.info_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "infoout.png")), size=(500, 100))
        self.login_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "login.png")), size=(300, 300))
        self.qrcode_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "qrcode.png")), size=(300, 300))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "user.png")), size=(30, 30))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Rework station", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=20, weight="bold"), text_color="red")
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="SETTINGS",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.settings_button_event)
        self.settings_button.grid(row=2, column=0, sticky="ew")

        self.data_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="DATA",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.data_button_event)
        self.data_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        
        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.login_frame.grid_columnconfigure(0, weight=1)
        
        self.login_frame_large_image_label = customtkinter.CTkLabel(self.login_frame, text="", image=self.large_login_image)
        self.login_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        self.login_frame_image_label = customtkinter.CTkLabel(self.login_frame, text="", image=self.login_image)
        self.login_frame_image_label.grid(row=1, column=0, padx=20, pady=10)
        
        # Login User Frame
        self.login_user_frame = customtkinter.CTkFrame(self.login_frame, corner_radius=0, fg_color="transparent")
        self.login_user_frame.grid(row=2, column=0, padx=20, pady=0)
        self.login_user_entry_label_1 = customtkinter.CTkLabel(self.login_user_frame,
                                                               text="Username: ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=25, weight="bold"),
                                                               text_color="blue")
        self.login_user_entry_label_1.grid(row=0, column=0, padx=10, pady=5)
        users = get_all("users")
        for user in users:
            self.list_users.append(user["username"])
        self.user_var = customtkinter.StringVar()
        self.login_frame_entry_1 = customtkinter.CTkComboBox(self.login_user_frame,
                                                            state='readonly',
                                                            values=self.list_users,
                                                            variable=self.user_var,
                                                            width=200)
        self.login_frame_entry_1.grid(row=0, column=1, padx=10, pady=0)
        
        
        # Login Password Frame
        self.login_pwd_frame = customtkinter.CTkFrame(self.login_frame, corner_radius=0, fg_color="transparent")
        self.login_pwd_frame.grid(row=3, column=0, padx=20, pady=5)
        self.login_pwd_entry_label_1 = customtkinter.CTkLabel(self.login_pwd_frame,
                                                               text="Password: ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=25, weight="bold"),
                                                               text_color="blue")
        self.login_pwd_entry_label_1.grid(row=0, column=0, padx=10, pady=5)
        self.login_frame_entry_2 = customtkinter.CTkEntry(self.login_pwd_frame, placeholder_text="Password",
                                                         height=30,
                                                         width=200,
                                                         font=("Helvetica", 25),
                                                         corner_radius=10,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         show='*')
        self.login_frame_entry_2.grid(row=0, column=1, padx=10, pady=0)
        
        # Login Button
        self.login_button = customtkinter.CTkButton(self.login_frame,
                                                    corner_radius=10,
                                                    height=60,
                                                    width=200,
                                                    border_spacing=10,
                                                    text="Login",
                                                    fg_color=("#066603"),
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.user_image,
                                                    font=customtkinter.CTkFont(size=20, weight="bold"),
                                                    command=self.login_button_event)
        self.login_button.grid(row=4, column=0, padx=20, pady=40)
        
        
        
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=1, column=0, padx=20, pady=0)

        self.home_frame_label = customtkinter.CTkLabel(self.home_frame,
                                                       text="",
                                                       image=self.info_image)
        self.home_frame_label.grid(row=2, column=0, padx=20, pady=0)
        self.home_frame_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.qrcode_image)
        self.home_frame_image_label.grid(row=3, column=0, padx=20, pady=10)
        
        # User Informations Frame
        self.info_user_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="orange")
        self.info_user_frame.grid(row=0, column=0, padx=20, pady=0)
        
        self.info_username_label = customtkinter.CTkLabel(self.info_user_frame,
                                                          text="Username : ",
                                                          compound="left",
                                                          font=customtkinter.CTkFont(size=20, weight="bold"),
                                                          text_color="blue")
        self.info_username_label.grid(row=0, column=0, padx=20, pady=0)
        self.info_usercard_label = customtkinter.CTkLabel(self.info_user_frame,
                                                          text="Usercard : ",
                                                          compound="left",
                                                          font=customtkinter.CTkFont(size=20, weight="bold"),
                                                          text_color="blue")
        self.info_usercard_label.grid(row=0, column=1, padx=20, pady=0)
        self.info_role_label = customtkinter.CTkLabel(self.info_user_frame,
                                                          text="role : ",
                                                          compound="left",
                                                          font=customtkinter.CTkFont(size=20, weight="bold"),
                                                          text_color="blue")
        self.info_role_label.grid(row=0, column=2, padx=20, pady=0)
        
        #rework Infos Frame
        self.rework_infos_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.rework_infos_frame.grid(row=0, column=0, padx=20, pady=0)
        self.home_frame_large_image_label1 = customtkinter.CTkLabel(self.rework_infos_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label1.grid(row=0, column=0, padx=20, pady=0)

        self.home_frame_label1 = customtkinter.CTkLabel(self.rework_infos_frame,
                                                       text="",
                                                       image=self.info_image)
        self.home_frame_label1.grid(row=1, column=0, padx=20, pady=0)
        
        self.fx_infos_frame = customtkinter.CTkFrame(self.rework_infos_frame, corner_radius=0, fg_color="transparent", border_width=1, border_color="black")
        self.fx_infos_frame.grid(row=2, column=0, padx=20, pady=0)
        self.fx_infos_label_1 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                         text="Reference: ",
                                                         compound="left",
                                                         font=customtkinter.CTkFont(size=25, weight="bold"),
                                                         text_color="blue")
        self.fx_infos_label_1.grid(row=0, column=0, padx=10, pady=5)
        self.fx_infos_label2 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Project: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label2.grid(row=1, column=0, padx=10, pady=5)
        self.fx_infos_label3 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Famille: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label3.grid(row=2, column=0, padx=10, pady=5)
        self.fx_infos_label4 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Car Type: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label4.grid(row=3, column=0, padx=10, pady=5)
        self.fx_infos_label10 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Reworker: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label10.grid(row=4, column=0, padx=10, pady=5)
        self.fx_infos_label5 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Line: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label5.grid(row=0, column=1, padx=10, pady=5)
        self.fx_infos_label6 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Supervisor: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label6.grid(row=1, column=1, padx=10, pady=5)
        self.fx_infos_label7 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Production Date: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label7.grid(row=2, column=1, padx=10, pady=5)
        self.fx_infos_label8 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Erreur: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="red")
        self.fx_infos_label8.grid(row=3, column=1, padx=10, pady=5)
        self.fx_infos_label9 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Erreur Details: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="red")
        self.fx_infos_label9.grid(row=4, column=1, padx=10, pady=5)
        self.fx_infos_label11 = customtkinter.CTkLabel(self.fx_infos_frame,
                                                        text="Rework Table: ",
                                                        compound="left",
                                                        font=customtkinter.CTkFont(size=25, weight="bold"),
                                                        text_color="blue")
        self.fx_infos_label11.grid(row=5, column=0, padx=10, pady=5)
        
        # Buttons Validation frame
        self.fx_validation_frame = customtkinter.CTkFrame(self.rework_infos_frame, corner_radius=0, fg_color="transparent")
        self.fx_validation_frame.grid(row=3, column=0, padx=20, pady=0)
        
        # Button Validation and Print
        self.validation_button = customtkinter.CTkButton(self.fx_validation_frame,
                                                           text="Validate Rework Rework",
                                                           font=customtkinter.CTkFont(size=17, weight="bold"),
                                                           command=self.on_submit,
                                                           fg_color=("green"),
                                                           height=50,
                                                           width=200)
        self.validation_button.grid(row=0, column=0, padx=20, pady=20)
        
        # Button Reject
        self.reject_button = customtkinter.CTkButton(self.fx_validation_frame,
                                                           text="Reject Rework",
                                                           font=customtkinter.CTkFont(size=17, weight="bold"),
                                                           command=self.on_reject,
                                                           fg_color=("red"),
                                                           height=50,
                                                           width=200)
        self.reject_button.grid(row=0, column=1, padx=20, pady=20)
        
        # scan QR code
        self.home_frame_entry_1 = customtkinter.CTkEntry(self.home_frame, placeholder_text="SCAN QR CODE LABEL",
                                                         height=50,
                                                         width=400,
                                                         font=("Helvetica", 30),
                                                         corner_radius=10,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         show='*')
        self.home_frame_entry_1.grid(row=4, column=0, padx=20, pady=0)
        
        # Button save and Print
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame,
                                                           text="Check Rework",
                                                           font=customtkinter.CTkFont(size=17, weight="bold"),
                                                           command=self.show_infos,
                                                           fg_color=("#066603"),
                                                           height=50,
                                                           width=200)
        self.home_frame_button_1.grid(row=5, column=0, padx=20, pady=20)
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("login")
        
        #enter key event
        self.login_frame_entry_1.bind("<Return>", self.login_button_event)
        self.home_frame_entry_1.bind("<Return>", self.on_submit)

    def on_submit(self, event=None):
        """save harness info"""
        label_data = {}
        label_data['OPERATOR'] = self.operator
        self.rework_obj.quality = self.operator
        label_data['PROJECT'] = self.rework_obj.project
        label_data['REFERENCE'] = self.rework_obj.ref
        self.rework_obj.status = "Finished"
        start_time = self.rework_obj.created_at
        end_time = datetime.now()
        
        rework_time = end_time - start_time
        rework_time = rework_time.total_seconds() / 60
        self.rework_obj.reworkduration = round(rework_time, 2)
        self.rework_obj.update()
        label_data['DATETIME'] = end_time.strftime("%Y-%m-%d %H:%M:%S")
        label_data['REWORKDATA'] = self.rework_obj.reworkcard
        label_data['REWORKTIME'] = round(rework_time, 2)
        
        # print Label
        generate_label(label_data['REWORKDATA'], 'end', label_data)
        # save data to csv
        self.select_frame_by_name("home")
        self.home_frame_entry_1.delete(0, customtkinter.END)

    def on_reject(self):
        self.select_frame_by_name("home")
        return
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")
        self.data_button.configure(fg_color=("gray75", "gray25") if name == "data" else "transparent")

        # show selected frame
        if name == "login":
            self.login_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.login_frame.grid_forget()
        if name == "home":
            self.info_username_label.configure(text= "Username : " + self.user["username"])
            self.info_usercard_label.configure(text= "Usercard : " + self.user["usercard"])
            self.info_role_label.configure(text= "Role : " + self.user["role"])
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "rework":
            self.rework_infos_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.rework_infos_frame.grid_forget()
        if name == "settings":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "data":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def login_button_event(self, event=None):
        self.operator = self.user_var.get()
        if self.operator == "":
            self.login_frame_entry_2.delete(0, customtkinter.END)
            self.login_frame_entry_1.set("")
            messagebox.showerror("Error", "Invalid Username!!!")
            self.operator = ""
            return
        self.password = self.login_frame_entry_2.get()
        self.user = get_obj("users", "username", self.operator)
        if self.user:
            if self.user["password"] == self.password:
                if self.user["role"] == "quality":
                    self.select_frame_by_name("home")
                    self.login_frame_entry_2.delete(0, customtkinter.END)
                    self.login_frame_entry_1.set("")
                else:
                    self.login_frame_entry_2.delete(0, customtkinter.END)
                    self.login_frame_entry_1.set("")
                    messagebox.showerror("Error", "Invalid Role!!!")
                    self.operator = ""
                    self.password = ""
                    return
            else:
                self.login_frame_entry_2.delete(0, customtkinter.END)
                self.login_frame_entry_1.set("")
                messagebox.showerror("Error", "Invalid Password!!!")
                self.operator = ""
                self.password = ""
                return
        else:
            self.login_frame_entry_2.delete(0, customtkinter.END)
            self.login_frame_entry_1.set("")
            messagebox.showerror("Error", "User Not Found!!!")
            self.operator = ""
            self.password = ""
            return

    def home_button_event(self):
        self.operator = ""
        self.select_frame_by_name("login")

    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def data_button_event(self):
        self.select_frame_by_name("data")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def clear_home_entries(self):
        """clear entries"""
        self.home_frame_entry_1.delete(0, customtkinter.END)
        self.home_frame_entry_2.delete(0, customtkinter.END)
        self.home_frame_entry_3.delete(0, customtkinter.END)
        self.home_frame_entry_4.delete(0, customtkinter.END)
        self.home_frame_entry_5.delete(0, customtkinter.END)
        self.home_frame_entry_6.delete(0, customtkinter.END)

    def show_infos(self):
        #check qrcode
        qr_code = self.home_frame_entry_1.get()
        rework_data = qr_code.split(';')
        if len(rework_data) < 2:
            self.home_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid QRCode!!!")
            return
        ref = get_obj("reference","ref", rework_data[1])
        if ref is None:
            self.home_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Reference!!!")
            return
        r_card = get_obj("reworkdetails", "reworkcard", rework_data[0])
        if r_card:
            if r_card["status"] == "Finished":
                self.home_frame_entry_1.delete(0, customtkinter.END)
                messagebox.showerror("Error", "FX Already Reworked!!!")
                return
            self.rework_obj = ReworkDetails(**r_card)
            self.fx_infos_label_1.configure(text= "Reference :" + r_card["ref"])
            self.fx_infos_label2.configure(text= "Project :" + r_card["project"])
            self.fx_infos_label3.configure(text= "Famille :" + r_card["famille"])
            self.fx_infos_label4.configure(text= "Car Type :" + r_card["car_type"])
            self.fx_infos_label5.configure(text= "Line :" + str(r_card["line"]))
            self.fx_infos_label6.configure(text= "Superviseur :" + r_card["superviseur"])
            self.fx_infos_label7.configure(text= "Production Date :" + str(r_card["prod_date"]))
            self.fx_infos_label8.configure(text= "Erreur :" + r_card["reworkfailure"])
            self.fx_infos_label9.configure(text= "Erreur Details :" + r_card["failuredetails"])
            self.fx_infos_label10.configure(text= "Reworker :" + r_card["reworker"])
            self.fx_infos_label11.configure(text= "Rework Table :" + str(r_card["reworktable"]))
            self.select_frame_by_name("rework")
            self.home_frame_entry_1.delete(0, customtkinter.END)
        else:
           self.home_frame_entry_1.delete(0, customtkinter.END)
           messagebox.showerror("Error", "FX Not Found!!!")
           return

if __name__ == "__main__":
    app = App()
    app.mainloop()