
import time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path="C:\Webdrivers\chromedriver.exe")


def open_site():
    driver.get("https://www.morfix.co.il/")
    driver.minimize_window()
    driver.implicitly_wait(5)


def valid_text(word):
    for i in word:
        if i.isdigit():
            return False
    return True


def click(event):
    word = str(input_box.get())
    translate(word)


def translate(word):
    if not valid_text(word) or len(word) == 0:
        print("Bad input")
        display_text1.set("Bad input")
        return
    driver.find_element(By.ID, "searchField").send_keys('')
    driver.find_element(By.ID, "searchField").send_keys(word)
    driver.find_element(By.ID, "searchField").send_keys(Keys.ENTER)

    delay = 10
    WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located)
    tran = driver.find_elements_by_class_name("Translation_spTop_heToen")
    defi = driver.find_elements_by_class_name("normal_translation_div")
    if len(tran) is 0 or len(defi) is 0:
        print("No translation available")
        display_text1.set("No translation available")
        return
    [print(tran[i].text + ':' + '\n' + defi[i].text) for i in range(len(tran))]
    time.sleep(1)

    display_text1.set(tran[0].text)
    display_text2.set(defi[0].text)
    time.sleep(2)


def clear():
    print("MENU COMMAND")


root = Tk()
root.title("Morfix Dictionary")
root.geometry("600x500")

menu = Menu(root)
root.config(menu=menu)
sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New", command=clear)
sub_menu.add_command(label="New Project", command=clear)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=exit(0))

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Inside Edit", command=lambda: print("INSIDE EDIT"))

# BACKGROUND IMAGE
# bg_img = PhotoImage(file="logo10.png")
Label(root, image=bg_img).place(relwidth=1, relheight=1)
Label(root, text="Enter a word in Hebrew to translate").pack()
input_box = Entry(root)
input_box.pack()
btn = Button(root, text="Translate!")
btn.pack()
display_text1 = StringVar()
lbl1 = Label(root, textvariable=display_text1)
lbl1.pack()
display_text2 = StringVar()
lbl2 = Label(root, textvariable=display_text2)
lbl2.pack()
btn.bind("<Button-1>", click)
open_site()
root.mainloop()
driver.quit()
