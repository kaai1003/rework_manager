import customtkinter
import os
from tkinter import messagebox
from PIL import Image

from datetime import datetime

from models.engine.database_manager import get_all
from models.engine.database_manager import get_obj
from models.reworkdetails import ReworkDetails

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("START REWORK STATION")
        self.geometry("1050x800")
        self.operator = ""
        self.list_users = []
        username = ""
        usercard = ""
        role = ""
        self.failures_list = ["Connexion endommagee",
                              "Erreur connexion",
                              "Joint dechire",
                              "Erreur de section de fils",
                              "Sertissage sur isolant",
                              "Erreur cosse",
                              "Exces de collle sur cosse",
                              "Manque etammage",
                              "Ergot de connexion manquant",
                              "Manchon mal positionnes",
                              "Manchon dechires",
                              "Erreur configuration",
                              "Erreur Manchon",
                              "Brains echapes",
                              "Bavure sur le srtissage",
                              "Contact manquant",
                              "Fil inverse",
                              "Fil coupe / casse",
                              "Connecteur non verrouille",
                              "Bouchon du connecteur dechire",
                              "Erreur de composant",
                              "Manque laniere de connecteur",
                              "Tube ecrase",
                              "Fil manquant",
                              "Erreur Gaine/Gaffe",
                              "Fil en plus",
                              "Manque relais",
                              "Manque Clip",
                              "Clip endommage",
                              "Mauvaise position de l'element",
                              "enrubannage non-conforme",
                              "BFRM endommage",
                              "Connecteur endommage",
                              "Gaine mal coupe/fissure",
                              "Branche trop courte",
                              "Branche trop longue",
                              "Fusible deforme",
                              "Fusible en mauvaise position",
                              "PIN deforme",
                              "Relais deforme",
                              "Relais en mauvaise position",
                              "Capot de connecteur casse",
                              "Noeud mal realise",
                              "Bavures / Fissures sur la surface",
                              "Corps etranger dans l'injection",
                              "Fils/gaine n'est pas au milieu de l'injection",
                              "Bulles d'air sur l'injection",
                              "Manque matiere / Non moule completement",
                              "Exces matiere sur la piece",
                              "Mauvaise matiere (granules)",
                              "Faute d'injection sur le passe-cable",
                              "Dechets sur la surface",
                              "Point d'injection trop long / mal arase",
                              "Piece surmoule non etanche",
                              "BFRM CASSE",
                              "BFRM ABIME",
                              "BOITIER CASSE",
                              "BOITIER ABIME",
                              "MANQUE MASSE"
                              ]

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "rework_icon.png")), size=(50, 50))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "start_rework.png")), size=(500, 170))
        self.large_login_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Rework-IN.png")), size=(500, 150))
        self.info_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "info.png")), size=(500, 100))
        self.login_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "login.png")), size=(300, 300))
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
        
        
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=1, column=0, padx=20, pady=0)

        self.home_frame_label = customtkinter.CTkLabel(self.home_frame,
                                                       text="",
                                                       image=self.info_image)
        self.home_frame_label.grid(row=2, column=0, padx=20, pady=0)
        
        #reference input Frame
        self.info_ref_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_ref_frame.grid(row=3, column=0, padx=0, pady=5)
        
        self.home_frame_entry_label_1 = customtkinter.CTkLabel(self.info_ref_frame,
                                                               text="Harness Reference :",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.home_frame_entry_label_1.grid(row=0, column=0, padx=20, pady=0)
        self.home_frame_entry_1 = customtkinter.CTkEntry(self.info_ref_frame, placeholder_text="ex: 1234567 01",
                                                         height=20,
                                                         width=300,
                                                         font=("Helvetica", 20),
                                                         corner_radius=5,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         border_color="#878bfa",
                                                         show='*')
        self.home_frame_entry_1.grid(row=0, column=1, padx=0, pady=0)
        
        #date production fx
        self.info_date_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_date_frame.grid(row=4, column=0, padx=0, pady=0)
        self.home_frame_entry_label_3 = customtkinter.CTkLabel(self.info_date_frame,
                                                               text="Date Production FX :      ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.home_frame_entry_label_3.grid(row=0, column=0, padx=0, pady=0)
        self.home_frame_entry_3 = customtkinter.CTkEntry(self.info_date_frame, placeholder_text="ex: 26-11-2024 12:10:10",
                                                         height=20,
                                                         width=300,
                                                         font=("Helvetica", 20),
                                                         corner_radius=5,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         border_color="#878bfa")
        self.home_frame_entry_3.grid(row=0, column=1, padx=0, pady=0)
        #Production Line
        self.info_line_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_line_frame.grid(row=5, column=0, padx=0, pady=0)
        self.home_frame_entry_label_4 = customtkinter.CTkLabel(self.info_line_frame,
                                                               text="Production Line :            ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.home_frame_entry_label_4.grid(row=0, column=0, padx=0, pady=5)
        self.home_frame_entry_4 = customtkinter.CTkEntry(self.info_line_frame, placeholder_text="ex : 1",
                                                         height=20,
                                                         width=300,
                                                         font=("Helvetica", 20),
                                                         corner_radius=5,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         border_color="#878bfa")
        self.home_frame_entry_4.grid(row=0, column=1, padx=0, pady=0)
        
        #Superviseur
        self.info_sup_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_sup_frame.grid(row=6, column=0, padx=0, pady=0)
        self.sup_label = customtkinter.CTkLabel(self.info_sup_frame,
                                                               text="Superviseur :                  ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.sup_label.grid(row=0, column=0, padx=0, pady=5)
        self.sup_var = customtkinter.StringVar()
        self.sup_entry = customtkinter.CTkComboBox(self.info_sup_frame,
                                                            state='readonly',
                                                            values=['LAD',
                                                                    'PTA',
                                                                    'Surmoulage',
                                                                    'BOL1',
                                                                    'BOL2',
                                                                    'Control Final',
                                                                    'CSL2'],
                                                            variable=self.sup_var,
                                                            width=300)
        self.sup_entry.grid(row=0, column=1, padx=0, pady=0)
        
        
        #rework input
        self.info_rework_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_rework_frame.grid(row=7, column=0, padx=0, pady=0)
        self.home_frame_entry_label_2 = customtkinter.CTkLabel(self.info_rework_frame,
                                                               text="Reword Card :      ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.home_frame_entry_label_2.grid(row=0, column=0, padx=0, pady=5)
        self.home_frame_entry_2 = customtkinter.CTkEntry(self.info_rework_frame, placeholder_text="Scan Rework Card",
                                                         height=20,
                                                         width=300,
                                                         font=("Helvetica", 20),
                                                         corner_radius=5,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         border_color="#878bfa",
                                                         show='*')
        self.home_frame_entry_2.grid(row=0, column=1, padx=0, pady=0)
        
        #Failure Type
        self.info_rework1_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_rework1_frame.grid(row=8, column=0, padx=0, pady=0)
        self.home_frame_entry_label_5 = customtkinter.CTkLabel(self.info_rework1_frame,
                                                               text="Failure Type :      ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.home_frame_entry_label_5.grid(row=0, column=0, padx=0, pady=5)
        self.subcategory_var = customtkinter.StringVar()
        self.home_frame_entry_5_sub = customtkinter.CTkComboBox(self.info_rework1_frame,
                                                                state='readonly',
                                                                values=self.failures_list,
                                                                variable=self.subcategory_var,
                                                                width=300)
        self.home_frame_entry_5_sub.grid(row=0, column=1, padx=0, pady=0)
        
        #Failure Details
        self.info_rework2_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_rework2_frame.grid(row=9, column=0, padx=0, pady=0)
        self.home_frame_entry_label_r = customtkinter.CTkLabel(self.info_rework2_frame,
                                                               text="Failure Description :      ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.home_frame_entry_label_r.grid(row=0, column=0, padx=0, pady=5)
        self.home_frame_entry_r = customtkinter.CTkEntry(self.info_rework2_frame, placeholder_text="ex : Connector name/Wire name/Clip name",
                                                         height=20,
                                                         width=300,
                                                         font=("Helvetica", 15),
                                                         corner_radius=5,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         border_color="#878bfa")
        self.home_frame_entry_r.grid(row=0, column=1, padx=0, pady=0)
        #Failure Process
        self.info_process_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_process_frame.grid(row=10, column=0, padx=0, pady=0)
        self.home_frame_entry_label_6 = customtkinter.CTkLabel(self.info_process_frame,
                                                               text="Failure Process :      ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.home_frame_entry_label_6.grid(row=0, column=0, padx=0, pady=5)
        self.process_var = customtkinter.StringVar()
        self.home_frame_entry_6 = customtkinter.CTkComboBox(self.info_process_frame,
                                                            state='readonly',
                                                            values=['LAD',
                                                                    'PTA',
                                                                    'Surmoulage',
                                                                    'BOL1',
                                                                    'BOL2',
                                                                    'Control Final',
                                                                    'CSL2'],
                                                            variable=self.process_var,
                                                            width=300)
        self.home_frame_entry_6.grid(row=0, column=1, padx=0, pady=0)
        
        #Rework Table
        self.info_table_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_table_frame.grid(row=11, column=0, padx=0, pady=0)
        self.rework_table_label = customtkinter.CTkLabel(self.info_table_frame,
                                                               text="Rework Table :      ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.rework_table_label.grid(row=0, column=0, padx=0, pady=5)
        self.table_var = customtkinter.StringVar()
        self.rework_table_entry = customtkinter.CTkComboBox(self.info_table_frame,
                                                            state='readonly',
                                                            values=['1',
                                                                    '2',
                                                                    '3',
                                                                    '4',
                                                                    '5'],
                                                            variable=self.table_var,
                                                            width=300)
        self.rework_table_entry.grid(row=0, column=1, padx=0, pady=0)
        
        #Reworker
        self.info_reworker_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.info_reworker_frame.grid(row=12, column=0, padx=0, pady=0)
        self.reworker_label = customtkinter.CTkLabel(self.info_reworker_frame,
                                                               text="Reworker Name :      ",
                                                               compound="left",
                                                               font=customtkinter.CTkFont(size=17, weight="bold"),
                                                               text_color="black")
        self.reworker_label.grid(row=0, column=0, padx=0, pady=5)
        self.reworker_var = customtkinter.StringVar()
        self.reworker_entry = customtkinter.CTkComboBox(self.info_reworker_frame,
                                                            state='readonly',
                                                            values=['1',
                                                                    '2',
                                                                    '3',
                                                                    '4',
                                                                    '5'],
                                                            variable=self.table_var,
                                                            width=300)
        self.reworker_entry.grid(row=0, column=1, padx=0, pady=0)
        
        # Button save and Print
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame,
                                                           text="Save and Print",
                                                           font=customtkinter.CTkFont(size=17, weight="bold"),
                                                           command=self.on_submit,
                                                           fg_color=("#066603"),
                                                           height=50,
                                                           width=200)
        self.home_frame_button_1.grid(row=15, column=0, padx=20, pady=20)
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("login")

        #enter key event
        self.login_frame_entry_1.bind("<Return>", self.login_button_event)
        self.home_frame_entry_2.bind("<Return>", self.on_submit)


    def on_submit(self, event=None):
        """save harness info"""
        rework_obj = None
        label_data = {}
        rework_data = {}
        label_data['OPERATOR'] = self.user["usercard"]
        rework_data["usercard"] = self.user["usercard"]
        # check Reference
        input_ref = self.home_frame_entry_1.get()
        if len(input_ref) <= 1:
            self.home_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Reference!!!")
            return
        ref = get_obj("reference","ref", input_ref[1:])
        if ref is None:
            self.home_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Reference!!!")
            return
        label_data['PROJECT'] = ref["project"] + "/" + ref["famille"]
        rework_data["ref"] = ref["ref"]
        rework_data["project"] = ref["project"]
        rework_data["famille"] = ref["famille"]
        rework_data["car_type"] = ref["car_type"]
        label_data['REFERENCE'] = ref["ref"]
        # check Production Line
        line = self.home_frame_entry_4.get()
        if line == '':
            self.home_frame_entry_4.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Production Line!!!")
            return
        rework_data["line"] = line
        # check Superviseur
        sup = self.sup_var.get()
        if sup == '':
            self.home_frame_entry_4.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid SuperViseur Name!!!")
            return
        rework_data["superviseur"] = sup
        # check Production Date
        date_prd = self.home_frame_entry_3.get()
        try:
            dt_prod = datetime.strptime(date_prd, "%d-%m-%Y %H:%M:%S")
        except Exception:
            self.home_frame_entry_3.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Date and Time!!!")
            return
        rework_data["prod_date"] = date_prd
        
        # Rework Card Check
        rework_card = self.home_frame_entry_2.get()
        if rework_card[0:1] == '*' and rework_card[-1] == '#':
            rework_card = rework_card[1:-1]
            data = get_obj("reworkdetails", "reworkcard", rework_card)
            if data:
                self.home_frame_entry_2.delete(0, customtkinter.END)
                messagebox.showerror("Error", "Harness Already Exist!!!")
                return
        else:
            self.home_frame_entry_2.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Rework Card!!!")
            return
        rework_data["reworkcard"] = rework_card
        # check Fault Description
        fault_desc = self.subcategory_var.get()
        if fault_desc == '':
            self.home_frame_entry_5.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Fault Description!!!")
            return
        rework_data["reworkfailure"] = fault_desc
        # check Fault Details
        rework_desc = self.home_frame_entry_r.get()
        if rework_desc == '':
            self.home_frame_entry_5.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Fault Description!!!")
            return
        rework_data["failuredetails"] = rework_desc
        # check Failure Process
        process = self.process_var.get()
        if process == '':
            self.home_frame_entry_6.delete(0, customtkinter.END)
            messagebox.showerror("Error", "InvalidProcess Step!!!")
            return
        rework_data["processfailure"] = process
        
        # check Rework Table
        rework_table = self.table_var.get()
        if rework_table == '':
            self.rework_table_entry.delete(0, customtkinter.END)
            messagebox.showerror("Error", "InvalidProcess Step!!!")
            return
        rework_data["reworktable"] = rework_table
        
        # check Reworker
        reworker_name = self.reworker_var.get()
        if rework_table == '':
            self.reworker_entry.delete(0, customtkinter.END)
            messagebox.showerror("Error", "InvalidProcess Step!!!")
            return
        rework_data["reworker"] = reworker_name
        rework_data["status"] = "Open"
        rework_obj = ReworkDetails(**rework_data)
        rework_obj.save()
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        label_data['DATETIME'] = start_time
        label_data['REWORKDATA'] = '{};{};{}'.format(rework_card,
                                                 ref["ref"],
                                                 start_time)
        
        # print Label
        #generate_label(rework_card, 'start', label_data)
        # save data to csv
        self.clear_home_entries()
        
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
                self.select_frame_by_name("home")
                self.login_frame_entry_2.delete(0, customtkinter.END)
                self.login_frame_entry_1.set("")
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
        self.home_frame_entry_5_sub.set("")
        self.home_frame_entry_6.set("")

if __name__ == "__main__":
    app = App()
    app.mainloop()