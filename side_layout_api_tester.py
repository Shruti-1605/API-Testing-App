import customtkinter as ctk
import requests
import json
import time
from tkinter import messagebox

# Side Layout API Tester
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("API Tester - Side Layout")
app.geometry("1200x700")

# === MAIN CONTAINER - SIDE BY SIDE ===
main_container = ctk.CTkFrame(app, fg_color="transparent")
main_container.pack(fill="both", expand=True, padx=10, pady=10)

# === LEFT SIDE - CONTROLS ===
left_frame = ctk.CTkFrame(main_container, width=500, fg_color="#F0F0F0")
left_frame.pack(side="left", fill="both", expand=False, padx=(0, 5))
left_frame.pack_propagate(False)

# Header
ctk.CTkLabel(left_frame, text="🚀 API Tester Controls", font=("Arial", 18, "bold")).pack(pady=10)

# URL Section
url_frame = ctk.CTkFrame(left_frame)
url_frame.pack(pady=5, padx=10, fill="x")
ctk.CTkLabel(url_frame, text="URL:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=2)
url_entry = ctk.CTkEntry(url_frame, placeholder_text="https://jsonplaceholder.typicode.com/posts/1", height=30)
url_entry.pack(padx=5, pady=5, fill="x")

# Method Section
method_frame = ctk.CTkFrame(left_frame)
method_frame.pack(pady=5, padx=10, fill="x")
ctk.CTkLabel(method_frame, text="Method:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=2)
method_option = ctk.CTkOptionMenu(method_frame, values=["GET", "POST", "PUT", "DELETE"], height=30)
method_option.pack(anchor="w", padx=5, pady=5)

# Headers Section
headers_frame = ctk.CTkFrame(left_frame)
headers_frame.pack(pady=5, padx=10, fill="x")
ctk.CTkLabel(headers_frame, text="Headers:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=2)
headers_text = ctk.CTkTextbox(headers_frame, height=60, font=("Courier", 10))
headers_text.insert("1.0", '{"Content-Type": "application/json"}')
headers_text.pack(padx=5, pady=5, fill="x")

# Body Section
body_frame = ctk.CTkFrame(left_frame)
body_frame.pack(pady=5, padx=10, fill="x")
ctk.CTkLabel(body_frame, text="Body:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=2)
body_text = ctk.CTkTextbox(body_frame, height=80, font=("Courier", 10))
body_text.insert("1.0", '{"title": "Test", "body": "API Test"}')
body_text.pack(padx=5, pady=5, fill="x")

# Buttons
button_frame = ctk.CTkFrame(left_frame)
button_frame.pack(pady=10, padx=10, fill="x")

send_btn = ctk.CTkButton(button_frame, text="🚀 SEND", width=100, height=40, font=("Arial", 14, "bold"))
send_btn.pack(side="left", padx=5)

clear_btn = ctk.CTkButton(button_frame, text="🗑️ Clear", width=80, height=40, fg_color="red")
clear_btn.pack(side="left", padx=5)

# === RIGHT SIDE - RESPONSE ===
right_frame = ctk.CTkFrame(main_container, fg_color="#E8F4FD")
right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

# Response Header
response_header = ctk.CTkFrame(right_frame, height=60, fg_color="#2196F3")
response_header.pack(fill="x", padx=10, pady=10)
response_header.pack_propagate(False)

ctk.CTkLabel(response_header, text="📊 API RESPONSE", font=("Arial", 20, "bold"), text_color="white").pack(expand=True)

# Status Bar
status_frame = ctk.CTkFrame(right_frame, height=40, fg_color="white")
status_frame.pack(fill="x", padx=10, pady=5)
status_frame.pack_propagate(False)

status_code_label = ctk.CTkLabel(status_frame, text="Status: Ready", font=("Arial", 12, "bold"))
status_code_label.pack(side="left", padx=10, pady=5)

time_label = ctk.CTkLabel(status_frame, text="Time: -", font=("Arial", 12))
time_label.pack(side="left", padx=10, pady=5)

size_label = ctk.CTkLabel(status_frame, text="Size: -", font=("Arial", 12))
size_label.pack(side="left", padx=10, pady=5)

# RESPONSE BOX - LARGE AND VISIBLE
response_box = ctk.CTkTextbox(
    right_frame,
    font=("Courier", 11),
    fg_color="white",
    text_color="black",
    border_width=2,
    border_color="#2196F3"
)
response_box.pack(pady=10, padx=10, fill="both", expand=True)
response_box.insert("1.0", "🔵 RESPONSE BOX - SIDE LAYOUT 🔵\n\nAPI response will appear here...\n\nThis box is guaranteed to be visible!\n\nEnter URL and click SEND to test API.")

# === FUNCTIONS ===
def send_request():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter URL!")
        return
    
    method = method_option.get()
    
    try:
        headers = json.loads(headers_text.get("1.0", "end-1c") or "{}")
    except:
        headers = {}
    
    try:
        body = json.loads(body_text.get("1.0", "end-1c") or "{}")
    except:
        body = {}
    
    # Clear and show loading
    response_box.delete("1.0", "end")
    response_box.insert("1.0", "⏳ Sending request...\nPlease wait...")
    app.update()
    
    try:
        start_time = time.time()
        
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=10)
        else:
            response = requests.request(method, url, headers=headers, json=body, timeout=10)
        
        elapsed = round(time.time() - start_time, 3)
        
        # Update status
        status_code_label.configure(text=f"Status: {response.status_code}")
        time_label.configure(text=f"Time: {elapsed}s")
        size_label.configure(text=f"Size: {len(response.content)}B")
        
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

def clear_response():
    response_box.delete("1.0", "end")
    response_box.insert("1.0", "Response cleared...")
    status_code_label.configure(text="Status: Ready")
    time_label.configure(text="Time: -")
    size_label.configure(text="Size: -")

# Connect buttons
send_btn.configure(command=send_request)
clear_btn.configure(command=clear_response)

# Keyboard shortcuts
app.bind("<Return>", lambda e: send_request())
app.bind("<Control-Return>", lambda e: send_request())

if __name__ == "__main__":
    app.mainloop()