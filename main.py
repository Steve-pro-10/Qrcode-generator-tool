import customtkinter as ctk
import qrcode 
import PIL#needed to display the qrcode in the program

root = ctk.CTk()

root.geometry("700x500")
root.title("QR Code Generator (1.0)")
def search_path():
    
    files = filedialog.askdirectory(title="Select the path where to save the qrcode")
    pathvariable.set(files)

def generate_qrcode():
    global image_label
    urlvariable_link = urlvariable.get()
    path = str(pathvariable.get())

    qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
	
    qr.add_data(urlvariable_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)

    print(f"The qrcode as been saved in {path}")

	
    equal_label = ctk.CTkImage(light_image=PIL.Image.open(path), size=(200, 200))
    image_label = ctk.CTkLabel(root,image=equal_label,text="")
    image_label.grid(column=1)

pathvariable = ctk.StringVar()
urlvariable = ctk.StringVar()

url_lb = ctk.CTkLabel(root, text="Qr Code's url")
url_lb.grid(row=0,column=1)
url = ctk.CTkEntry(root,textvariable=urlvariable,width=350,height=20)
url.grid(row=1, column=1)

path = ctk.CTkEntry(root,textvariable=pathvariable,width=350,height=20)
path.grid(row=2, column=1)

path_button = ctk.CTkButton(root, text="search path",command=search_path)
path_button.grid(row=2,column=2)
button = ctk.CTkButton(root,text="generate",command=generate_qrcode)
button.grid(row=3,column=1)


root.mainloop()
