'''
# Name: expense_manager.py
# Aim: To implement functions for the Expense Manager project. This will be used in main_ui.py
# Start date: 14.June 2021
# End date: ---
# Library/Frameworks used: PyQt5, Pandas, Matplotlib
'''
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
import datetime as dt

class ExpMngr():

    def __init__(self):
        print("["+str(dt.datetime.now())+"]"+" : Class ExpMngr called")

    def create_buttons(self, button_text, l_margin, r_margin, colour_code):
        button = QPushButton(button_text)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(500)
        button.setStyleSheet("*{border: 4px solid '"+str(colour_code)+"';" +
                             "margin-left:" + str(l_margin) + "px;" +
                             "margin-right:" + str(r_margin) + "px;" +
                             "color: 'white';" +
                             "font-family: 'shanti';" +
                             "font-size: 16px;" +
                             "border-radius: 25px;" +
                             "padding: 15px 0px;" +
                             "margin: 100px 20px;}" +
                             "*:hover{background: '"+str(colour_code)+"';}")
        return button

    def app_logo_placement(self):   # function for showing the app logo at the top
        app_logo = QPixmap("app_logo.png")
        app_logo_label = QLabel()
        app_logo_label.setPixmap(app_logo.scaled(80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        app_logo_label.setAlignment(QtCore.Qt.AlignLeft)
        return app_logo_label

    def input_page_window(self):
        exp_mngr_window = QWidget()
        exp_mngr_window.setWindowTitle("Input your expenses-Expense Manager")
        exp_mngr_window.setStyleSheet("background: '#000000'")
        exp_mngr_window.setFixedWidth(1600)
        exp_mngr_window.setFixedHeight(1000)
        print("[" + str(dt.datetime.now()) + "]" + " : Input page window creation successful!")
        return exp_mngr_window

    def input_page_frame_grid(self):
        grid = QGridLayout()
        return grid

    def homepage_window(self):
        exp_mngr_window = QWidget()
        exp_mngr_window.setWindowTitle("Homepage-Expense Manager")
        exp_mngr_window.setStyleSheet("background: '#000000'")
        exp_mngr_window.setFixedWidth(1600)
        exp_mngr_window.setFixedHeight(1000)
        print("[" + str(dt.datetime.now()) + "]" + " : Homepage window creation successful!")
        return exp_mngr_window

    def homepage_frame_grid(self):
        grid_homepage = QGridLayout()
        homepage_image = QPixmap("homepage_image_scaled.png")
        homepage_image_label = QLabel()
        homepage_image_label.setPixmap(homepage_image)
        homepage_image_label.setAlignment(QtCore.Qt.AlignCenter)
        # homepage_image_label.setStyleSheet("margin-top:75px; margin-bottom:30px;")
        input_button = self.create_buttons("Enter Expense (in €)", 85, 5, "#00FF00")
        stats_button = self.create_buttons("Show Stats (Monthly, Weekly)", 5, 85, "#FF0000")
        overview_button = self.create_buttons("Show annual overview", 85, 5, "#FF00FF")
        download_report_button = self.create_buttons("Data in TXT format", 5, 85, "#808080")
        app_logo = self.app_logo_placement()
        grid_homepage.addWidget(app_logo, 0, 0, 1, 1)
        grid_homepage.addWidget(input_button, 2, 0)
        grid_homepage.addWidget(stats_button, 2, 1)
        grid_homepage.addWidget(overview_button, 3, 0)
        grid_homepage.addWidget(download_report_button, 3, 1)
        grid_homepage.addWidget(homepage_image_label, 0, 0, 1, 2)
        print("[" + str(dt.datetime.now()) + "]" + " : Homepage grid creation successful!")
        return grid_homepage



