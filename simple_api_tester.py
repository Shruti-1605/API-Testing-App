import customtkinter as ctk
import requests
import json
import time
from tkinter import messagebox

# Simple API Tester with Visible Response Box
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Simple API Tester")
app.geometry("800x700")

# URL Section
url_frame = ctk.CTkFrame(app)
url_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(url_frame, text="API URL:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
url_entry = ctk.CTkEntry(url_frame, placeholder_text="https://jsonplaceholder.typicode.com/posts/1", width=600, height=35)
url_entry.pack(padx=10, pady=5, fill="x")

# Method Section
method_frame = ctk.CTkFrame(app)
method_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(method_frame, text="Method:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=5)
method_option = ctk.CTkOptionMenu(method_frame, values=["GET", "POST", "PUT", "DELETE"], width=150, height=35)
method_option.pack(anchor="w", padx=10, pady=5)

# Send Button
send_btn = ctk.CTkButton(app, text="🚀 SEND REQUEST", width=200, height=50, font=("Arial", 16, "bold"))
send_btn.pack(pady=20)

# Response Section - LARGE AND VISIBLE
response_frame = ctk.CTkFrame(app, fg_color="lightgray")
response_frame.pack(pady=10, padx=20, fill="both", expand=True)

ctk.CTkLabel(response_frame, text="📊 API RESPONSE", font=("Arial", 16, "bold")).pack(pady=10)

# Status Info
status_info_frame = ctk.CTkFrame(response_frame, fg_color="white")
status_info_frame.pack(pady=5, padx=10, fill="x")

status_code_label = ctk.CTkLabel(status_info_frame, text="Status: Ready", font=("Arial", 12))
status_code_label.pack(side="left", padx=10, pady=5)

time_label = ctk.CTkLabel(status_info_frame, text="Time: -", font=("Arial", 12))
time_label.pack(side="left", padx=10, pady=5)

# RESPONSE BOX - GUARANTEED VISIBLE
response_box = ctk.CTkTextbox(
    response_frame,
    width=700,
    height=300,
    font=("Courier", 12),
    fg_color="white",
    text_color="black",
    border_width=3,
    border_color="blue"
)
response_box.pack(pady=10, padx=10, fill="both", expand=True)
response_box.insert("1.0", "🔵 RESPONSE BOX IS VISIBLE! 🔵\n\nAPI response will appear here...\n\nEnter URL and click SEND REQUEST")

def send_request():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter URL!")
        return
    
    method = method_option.get()
    
    # Clear and show loading
    response_box.delete("1.0", "end")
    response_box.insert("1.0", "⏳ Sending request...\nPlease wait...")
    app.update()
    
    try:
        start_time = time.time()
        
        if method == "GET":
            response = requests.get(url, timeout=10)
        else:
            response = requests.request(method, url, timeout=10)
        
        elapsed = round(time.time() - start_time, 3)
        
        # Update status
        status_code_label.configure(text=f"Status: {response.status_code}")
        time_label.configure(text=f"Time: {elapsed}s")
        
        # Show response
        response_box.delete("1.0", "end")
        
        try:
            json_data = response.json()
            formatted = json.dumps(json_data, indent=2)
            response_box.insert("1.0", formatted)
        except:
            response_box.insert("1.0", response.text)
            
    except Exception as e:
        response_box.delete("1.0", "end")
        response_box.insert("1.0", f"❌ Error: {str(e)}")
        status_code_label.configure(text="Status: Error")

# Connect button
send_btn.configure(command=send_request)

# Keyboard shortcut
app.bind("<Return>", lambda e: send_request())

if __name__ == "__main__":
    app.mainloop()