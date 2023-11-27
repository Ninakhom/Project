import tkinter
import mysql.connector as mysql
from tkinter import messagebox
import os

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800")