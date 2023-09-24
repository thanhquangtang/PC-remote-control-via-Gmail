from tkinter import *
from PIL import Image, ImageTk
from client import *

border_bg = "black"
border_thick = 2
email = ""

root = Tk()
root.title("TELEPC WITH GMAIL API (Group 9)")
root.geometry("800x600")

def drawMAC():
    MAC_menu = Toplevel(root)
    MAC_menu.geometry("400x400")

    labelEmail = Label(MAC_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e = Entry(MAC_menu, width=50, borderwidth=5)
    e.pack()

    def clickMACImage():
        global email
        email = e.get()
        sendMAC(email)
        labelSuccess = Label(MAC_menu, text="Successfully sent MAC address request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("mac.png").resize((100,100))
    MACimg = ImageTk.PhotoImage(img)
    border = Frame(MAC_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    MACButton = Button(border, image=MACimg, command=clickMACImage)
    MACButton.image = MACimg
    MACButton.pack()
    border.pack()

def drawShutdown():
    Shutdown_menu = Toplevel(root)
    Shutdown_menu.geometry("400x400")

    labelEmail = Label(Shutdown_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e = Entry(Shutdown_menu, width=50, borderwidth=5)
    e.pack()

    def clickShutdownImage():
        global email
        email = e.get()
        sendShutdown(email)
        labelSuccess = Label(root, text="Successfully sent shutdown request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("shutdown.png").resize((100,100))
    Shutdownimg = ImageTk.PhotoImage(img)
    Shutdownbutton_border = Frame(Shutdown_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    ShutdownButton = Button(Shutdownbutton_border, image=Shutdownimg, command=clickShutdownImage)
    ShutdownButton.image = Shutdownimg
    ShutdownButton.pack()
    Shutdownbutton_border.pack()

def drawLogout():
    Logout_menu = Toplevel(root)
    Logout_menu.geometry("400x400")

    labelEmail = Label(Logout_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e = Entry(Logout_menu, width=50, borderwidth=5)
    e.pack()

    def clickLogoutImage():
        global email
        email = e.get()
        sendLogout(email)
        labelSuccess = Label(Logout_menu, text="Successfully sent logout request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("logout.png").resize((100,100))
    Logoutimg = ImageTk.PhotoImage(img)
    border = Frame(Logout_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    ShutdownButton = Button(border, image=Logoutimg, command=clickLogoutImage)
    ShutdownButton.image = Logoutimg
    ShutdownButton.pack()
    border.pack()

def drawLivescreen():
    Livescreen_menu = Toplevel(root)
    Livescreen_menu.geometry("400x400")

    labelEmail = Label(Livescreen_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e = Entry(Livescreen_menu, width=50, borderwidth=5)
    e.pack()

    def clickLivescreenImage():
        global email
        email = e.get()
        sendLivescreen(email)
        labelSuccess = Label(Livescreen_menu, text="Successfully sent live screen capture request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("livescreen.png").resize((100,100))
    Livescreenimg = ImageTk.PhotoImage(img)
    border = Frame(Livescreen_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    LivescreenButton = Button(border, image=Livescreenimg, command=clickLivescreenImage)
    LivescreenButton.image = Livescreenimg
    LivescreenButton.pack()
    border.pack()

def drawLoadRegistry():
    LoadRegistry_menu = Toplevel(root)
    LoadRegistry_menu.geometry("400x400")

    labelEmail = Label(LoadRegistry_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e1 = Entry(LoadRegistry_menu, width=50, borderwidth=5)
    e1.pack()

    labelContent = Label(LoadRegistry_menu, text="Enter registry", font=("Arial", 20), pady=10)
    labelContent.pack()

    e2 = Entry(LoadRegistry_menu, width=50, borderwidth=5)
    e2.pack()

    def clickLoadRegistryImage():
        global email
        email = e1.get()
        content = e2.get()
        sendLoadRegistry(email, content)
        labelSuccess = Label(LoadRegistry_menu, text="Successfully sent load registry request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("loadregistry.png").resize((100,100))
    LoadRegistryimg = ImageTk.PhotoImage(img)
    border = Frame(LoadRegistry_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    LoadRegistryButton = Button(border, image=LoadRegistryimg, command=clickLoadRegistryImage)
    LoadRegistryButton.image = LoadRegistryimg
    LoadRegistryButton.pack()
    border.pack()

def drawSaveRegistry():
    SaveRegistry_menu = Toplevel(root)
    SaveRegistry_menu.geometry("400x400")

    labelEmail = Label(SaveRegistry_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e = Entry(SaveRegistry_menu, width=50, borderwidth=5)
    e.pack()

    def clickSaveRegistryImage():
        global email
        email = e.get()
        sendSaveRegistry(email)
        labelSuccess = Label(SaveRegistry_menu, text="Successfully sent save registry request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("saveregistry.png").resize((100,100))
    SaveRegistryimg = ImageTk.PhotoImage(img)
    border = Frame(SaveRegistry_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    SaveRegistryButton = Button(border, image=SaveRegistryimg, command=clickSaveRegistryImage)
    SaveRegistryButton.image = SaveRegistryimg
    SaveRegistryButton.pack()
    border.pack()

def drawAppProcess():
    AppProcess_menu = Toplevel(root)
    AppProcess_menu.geometry("400x400")

    labelEmail = Label(AppProcess_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e = Entry(AppProcess_menu, width=50, borderwidth=5)
    e.pack()

    def clickAppProcessImage():
        global email
        email = e.get()
        sendAppProcess(email)
        labelSuccess = Label(AppProcess_menu, text="Successfully sent app process request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("appprocess.png").resize((100,100))
    AppProcessimg = ImageTk.PhotoImage(img)
    border = Frame(AppProcess_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    AppProcessButton = Button(border, image=AppProcessimg, command=clickAppProcessImage)
    AppProcessButton.image = AppProcessimg
    AppProcessButton.pack()
    border.pack()

def drawDirectoryTree():
    DirectoryTree_menu = Toplevel(root)
    DirectoryTree_menu.geometry("400x400")

    labelEmail = Label(DirectoryTree_menu, text="Enter target email", font=("Arial", 20), pady=10)
    labelEmail.pack()

    e1 = Entry(DirectoryTree_menu, width=50, borderwidth=5)
    e1.pack()

    labelContent = Label(DirectoryTree_menu, text="Enter directory head", font=("Arial", 20), pady=10)
    labelContent.pack()

    e2 = Entry(DirectoryTree_menu, width=50, borderwidth=5)
    e2.pack()

    def clickDirectoryTreeImage():
        global email
        email = e1.get()
        content = e2.get()
        sendDirectoryTree(email, content)
        labelSuccess = Label(DirectoryTree_menu, text="Successfully sent directory tree request to " + email, fg="green")
        labelSuccess.pack()

    img = Image.open("dir.png").resize((100,100))
    DirectoryTreeimg = ImageTk.PhotoImage(img)
    border = Frame(DirectoryTree_menu, highlightbackground = border_bg, highlightthickness = border_thick, bd=0)
    DirectoryTreeButton = Button(border, image=DirectoryTreeimg, command=clickDirectoryTreeImage)
    DirectoryTreeButton.image = DirectoryTreeimg
    DirectoryTreeButton.pack()
    border.pack()
   
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Get MAC address", command=drawMAC)
filemenu.add_command(label="Shut down PC", command=drawShutdown)
filemenu.add_command(label="Log out PC", command=drawLogout)
filemenu.add_command(label="Live screen capture", command=drawLivescreen)
filemenu.add_command(label="Load registry", command=drawLoadRegistry)
filemenu.add_command(label="Save registry", command=drawSaveRegistry)
filemenu.add_command(label="App process", command=drawAppProcess)
filemenu.add_command(label="Directory tree", command=drawDirectoryTree)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Main menu", menu=filemenu)

myTitle = Label(root, text="TELEPC WITH GMAIL API", font=("Arial", 25), pady=20)
myTitle.pack()

img = Image.open("gmail.jpg").resize((125,125))
Gmailimg = ImageTk.PhotoImage(img)
myImg = Label(root, image=Gmailimg)
myImg.pack()

myGroupInfo = Label(root, text="Made by GROUP 9\nLâm Trí Đức - 19127122\nThái Duy Nguyễn - 19127054\nTăng Thanh Quang - 19127531", font=("Arial", 20), pady=20)
myGroupInfo.pack()

extraInfo = Label(root, text="Go to Main menu Tab to start using functions !", font=("Arial", 20), pady=20)
extraInfo.pack()

root.config(menu=menubar)
root.mainloop()