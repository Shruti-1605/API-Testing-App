import customtkinter as ctk
import requests
import json
import time
import os
from datetime import datetime
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# === PROFESSIONAL SETTINGS ===
current_theme = "light"
ctk.set_appearance_mode(current_theme)
ctk.set_default_color_theme("blue")

# Professional Color Palette
COLORS = {
    "primary": "#1E3A8A",      # Deep Blue
    "secondary": "#3B82F6",    # Blue
    "accent": "#10B981",       # Emerald
    "warning": "#F59E0B",      # Amber
    "danger": "#EF4444",       # Red
    "success": "#22C55E",      # Green
    "dark": "#1F2937",         # Dark Gray
    "light": "#F8FAFC",        # Light Gray
    "white": "#FFFFFF",
    "border": "#E5E7EB"
}

# === MAIN WINDOW ===
app = ctk.CTk()
app.title("API Tester Pro - Professional Edition")
app.geometry("1200x700")
app.resizable(True, True)
app.minsize(1000, 600)

# === MAIN CONTAINER - SIDE BY SIDE ===
app.configure(fg_color="#BBDEFB")  # Slightly darker blue background
main_container = ctk.CTkFrame(app, fg_color="transparent")
main_container.pack(fill="both", expand=True, padx=10, pady=10)

# === LEFT SIDE - CONTROLS ===
left_frame = ctk.CTkFrame(main_container, width=500, fg_color="#E1F5FE")
left_frame.pack(side="left", fill="both", expand=False, padx=(0, 5))
left_frame.pack_propagate(False)

# === PROFESSIONAL HEADER ===
header = ctk.CTkFrame(left_frame, fg_color=COLORS["primary"], corner_radius=15, height=90)
header.pack(pady=10, padx=10, fill="x")
header.pack_propagate(False)

# Logo and Title Container
title_container = ctk.CTkFrame(header, fg_color="transparent")
title_container.pack(side="left", fill="both", expand=True, padx=20, pady=15)

title = ctk.CTkLabel(
    title_container,
    text="🚀 API Tester Pro",
    font=("Segoe UI", 28, "bold"),
    text_color="white"
)
title.pack(anchor="w")

subtitle = ctk.CTkLabel(
    title_container,
    text="Professional API Testing Suite",
    font=("Segoe UI", 12),
    text_color="#93C5FD"
)
subtitle.pack(anchor="w")

# Professional Theme Toggle
theme_container = ctk.CTkFrame(header, fg_color="transparent")
theme_container.pack(side="right", padx=20, pady=15)

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    ctk.set_appearance_mode(current_theme)
    theme_btn.configure(text="☀️" if current_theme == "dark" else "🌙")
    
    # Update background colors for dark mode
    if current_theme == "dark":
        app.configure(fg_color="#1a1a1a")  # Dark background
        left_frame.configure(fg_color="#2d2d2d")  # Dark left frame
        right_frame.configure(fg_color="#2d2d2d")  # Dark right frame
        response_frame.configure(fg_color="#3d3d3d")  # Dark response frame
    else:
        app.configure(fg_color="#BBDEFB")  # Light blue background
        left_frame.configure(fg_color="#E1F5FE")  # Light blue left frame
        right_frame.configure(fg_color="#E1F5FE")  # Light blue right frame
        response_frame.configure(fg_color="lightgray")  # Light gray response frame

theme_btn = ctk.CTkButton(
    theme_container,
    text="🌙" if current_theme == "light" else "☀️",
    command=toggle_theme,
    width=50,
    height=50,
    font=("Segoe UI", 18),
    fg_color="#FFFFFF",
    hover_color="#F0F0F0",
    corner_radius=25,
    text_color=COLORS["primary"]
)
theme_btn.pack()

# === PROFESSIONAL URL SECTION ===
url_section = ctk.CTkFrame(left_frame, corner_radius=15, fg_color=COLORS["white"], border_width=1, border_color=COLORS["border"])
url_section.pack(pady=5, padx=10, fill="x")

url_header = ctk.CTkFrame(url_section, fg_color=COLORS["light"], corner_radius=10, height=40)
url_header.pack(pady=12, padx=12, fill="x")
url_header.pack_propagate(False)

ctk.CTkLabel(url_header, text="🔗 API Endpoint", font=("Segoe UI", 16, "bold"), text_color=COLORS["dark"]).pack(expand=True)

url_entry = ctk.CTkEntry(
    url_section, 
    height=40, 
    placeholder_text="https://jsonplaceholder.typicode.com/posts/1",
    font=("Segoe UI", 12), 
    corner_radius=10,
    border_width=2,
    border_color=COLORS["border"]
)
url_entry.pack(pady=(0, 12), padx=12, fill="x")

# === PROFESSIONAL METHOD & HEADERS ROW ===
method_headers_row = ctk.CTkFrame(left_frame, fg_color="transparent")
method_headers_row.pack(pady=5, padx=10, fill="x")

# Method Section
method_section = ctk.CTkFrame(method_headers_row, corner_radius=15, fg_color=COLORS["white"], border_width=1, border_color=COLORS["border"])
method_section.pack(side="left", fill="both", expand=True, padx=(0, 8))

method_header = ctk.CTkFrame(method_section, fg_color=COLORS["light"], corner_radius=10, height=35)
method_header.pack(pady=10, padx=10, fill="x")
method_header.pack_propagate(False)

ctk.CTkLabel(method_header, text="📋 Method", font=("Segoe UI", 14, "bold"), text_color=COLORS["dark"]).pack(expand=True)
    
method_option = ctk.CTkOptionMenu(
    method_section, 
    values=["GET", "POST", "PUT", "DELETE", "PATCH"],
    height=35, 
    font=("Segoe UI", 12, "bold"), 
    corner_radius=10,
    fg_color=COLORS["secondary"],
    button_color=COLORS["primary"],
    button_hover_color=COLORS["dark"]
)
method_option.pack(pady=(0, 10), padx=10, fill="x")

# Quick Headers Section
quick_headers_section = ctk.CTkFrame(method_headers_row, corner_radius=15, fg_color=COLORS["white"], border_width=1, border_color=COLORS["border"])
quick_headers_section.pack(side="right", fill="both", expand=True, padx=(8, 0))

quick_header = ctk.CTkFrame(quick_headers_section, fg_color=COLORS["light"], corner_radius=10, height=35)
quick_header.pack(pady=10, padx=10, fill="x")
quick_header.pack_propagate(False)

ctk.CTkLabel(quick_header, text="⚡ Quick Headers", font=("Segoe UI", 14, "bold"), text_color=COLORS["dark"]).pack(expand=True)

def set_quick_headers(choice):
    headers_map = {
        "JSON": '{\n  "Content-Type": "application/json",\n  "Accept": "application/json"\n}',
        "Form Data": '{\n  "Content-Type": "application/x-www-form-urlencoded"\n}',
        "XML": '{\n  "Content-Type": "application/xml",\n  "Accept": "application/xml"\n}',
        "Plain Text": '{\n  "Content-Type": "text/plain"\n}'
    }
    headers_text.delete("1.0", "end")
    headers_text.insert("1.0", headers_map.get(choice, "{}"))

headers_option = ctk.CTkOptionMenu(
    quick_headers_section,
    values=["JSON", "Form Data", "XML", "Plain Text"],
    height=35,
    font=("Segoe UI", 12, "bold"),
    corner_radius=10,
    fg_color=COLORS["accent"],
    button_color=COLORS["success"],
    button_hover_color=COLORS["dark"],
    command=set_quick_headers
)
headers_option.pack(pady=(0, 10), padx=10, fill="x")

# === PROFESSIONAL HEADERS SECTION ===
headers_section = ctk.CTkFrame(left_frame, corner_radius=15, fg_color=COLORS["white"], border_width=1, border_color=COLORS["border"])
headers_section.pack(pady=5, padx=10, fill="x")

headers_header = ctk.CTkFrame(headers_section, fg_color=COLORS["light"], corner_radius=10, height=35)
headers_header.pack(pady=10, padx=10, fill="x")
headers_header.pack_propagate(False)

ctk.CTkLabel(headers_header, text="📄 Request Headers", font=("Segoe UI", 14, "bold"), text_color=COLORS["dark"]).pack(expand=True)

headers_text = ctk.CTkTextbox(
    headers_section, 
    height=70, 
    font=("Consolas", 10), 
    corner_radius=10,
    border_width=1,
    border_color=COLORS["border"]
)
headers_text.insert("1.0", '{\n  "Content-Type": "application/json",\n  "Accept": "application/json"\n}')
headers_text.pack(pady=(0, 10), padx=10, fill="x")

# === PROFESSIONAL BODY SECTION ===
body_section = ctk.CTkFrame(left_frame, corner_radius=15, fg_color=COLORS["white"], border_width=1, border_color=COLORS["border"])
body_section.pack(pady=5, padx=10, fill="x")

body_header = ctk.CTkFrame(body_section, fg_color=COLORS["light"], corner_radius=10, height=35)
body_header.pack(pady=10, padx=10, fill="x")
body_header.pack_propagate(False)

ctk.CTkLabel(body_header, text="📦 Request Body", font=("Segoe UI", 14, "bold"), text_color=COLORS["dark"]).pack(expand=True)

body_text = ctk.CTkTextbox(
    body_section, 
    height=80, 
    font=("Consolas", 10), 
    corner_radius=10,
    border_width=1,
    border_color=COLORS["border"]
)
body_text.insert("1.0", '{\n  "title": "Sample Post",\n  "body": "Professional API Testing",\n  "userId": 1\n}')
body_text.pack(pady=(0, 10), padx=10, fill="x")

# === PROFESSIONAL ACTION BUTTONS ===
action_section = ctk.CTkFrame(left_frame, fg_color="transparent")
action_section.pack(pady=10, padx=10, fill="x")

# Primary Actions Row
primary_row = ctk.CTkFrame(action_section, fg_color="transparent")
primary_row.pack(pady=5)

def send_request():
    url = url_entry.get().strip()
    if not url:
        status_label.configure(text="❌ Please enter a valid URL", text_color=COLORS["danger"])
        return
        
    method = method_option.get()
    
    try:
        headers = json.loads(headers_text.get("1.0", "end-1c") or "{}")
    except json.JSONDecodeError:
        status_label.configure(text="❌ Invalid JSON format in headers", text_color=COLORS["danger"])
        return
        
    try:
        body = json.loads(body_text.get("1.0", "end-1c") or "{}")
    except json.JSONDecodeError:
        if method in ["POST", "PUT", "PATCH"]:
            status_label.configure(text="❌ Invalid JSON format in body", text_color=COLORS["danger"])
            return
        body = {}

    # Clear previous response
    response_box.delete("1.0", "end")
    status_code_label.configure(text="")
    time_label.configure(text="")
    size_label.configure(text="")
    
    # Professional loading state
    response_box.insert("end", "⏳ Sending request...\n🔄 Processing your API call...")
    status_label.configure(text="⏳ Processing request...", text_color=COLORS["warning"])
    app.update()

    start_time = time.time()
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=30)
        else:
            response = requests.request(method, url, headers=headers, json=body, timeout=30)
            
        elapsed = round(time.time() - start_time, 3)
        response_size = len(response.content)
        
        # Professional status display
        status_code_color = COLORS["success"] if 200 <= response.status_code < 300 else COLORS["danger"]
        status_code_label.configure(text=f"Status: {response.status_code}", text_color=status_code_color)
        time_label.configure(text=f"Time: {elapsed}s", text_color=COLORS["dark"])
        size_label.configure(text=f"Size: {response_size}B", text_color=COLORS["dark"])
        
        # Clear and show professional response
        response_box.delete("1.0", "end")
        
        try:
            json_response = response.json()
            formatted = json.dumps(json_response, indent=2, ensure_ascii=False)
        except:
            formatted = response.text
            
        response_box.insert("end", formatted)
        
        # Save to history
        save_to_history(url, method, headers, body, response.status_code, elapsed, formatted)
        
        # Update API status indicator
        if 200 <= response.status_code < 300:
            api_status_label.configure(text="🟢 API Success", text_color="green")
        else:
            api_status_label.configure(text="🔴 API Failed", text_color="red")
        
        status_label.configure(text="✅ Request completed successfully", text_color=COLORS["success"])
        
    except requests.exceptions.Timeout:
        response_box.delete("1.0", "end")
        response_box.insert("end", "⏰ Request timed out (30s limit)")
        api_status_label.configure(text="🔴 API Failed", text_color="red")
        status_label.configure(text="⏰ Request timeout", text_color=COLORS["warning"])
        
    except requests.exceptions.ConnectionError:
        response_box.delete("1.0", "end")
        response_box.insert("end", "🔌 Connection error - Check your internet or URL")
        api_status_label.configure(text="🔴 API Failed", text_color="red")
        status_label.configure(text="🔌 Connection failed", text_color=COLORS["danger"])
        
    except Exception as e:
        response_box.delete("1.0", "end")
        response_box.insert("end", f"❌ Error: {str(e)}")
        api_status_label.configure(text="🔴 API Failed", text_color="red")
        status_label.configure(text="❌ Request failed", text_color=COLORS["danger"])

def clear_response():
    response_box.delete("1.0", "end")
    status_code_label.configure(text="")
    time_label.configure(text="")
    size_label.configure(text="")
    api_status_label.configure(text="🟡 Cleared", text_color="orange")
    status_label.configure(text="🗑️ Response cleared", text_color=COLORS["warning"])

def save_response():
    content = response_box.get("1.0", "end-1c")
    if not content.strip():
        status_label.configure(text="❌ No response to save", text_color=COLORS["danger"])
        return
        
    try:
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            status_label.configure(text="💾 Response saved successfully", text_color=COLORS["success"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save: {e}")

def save_to_history(url, method, headers, body, status_code, response_time, response_data):
    try:
        os.makedirs("data", exist_ok=True)
        history_file = "data/history.json"
        
        history_entry = {
            "timestamp": datetime.now().isoformat(),
            "url": url,
            "method": method,
            "headers": headers,
            "body": body,
            "status_code": status_code,
            "response_time": response_time,
            "response_data": response_data[:500] + "..." if len(response_data) > 500 else response_data
        }
        
        if os.path.exists(history_file):
            with open(history_file, "r", encoding="utf-8") as f:
                history = json.load(f)
        else:
            history = []
            
        history.insert(0, history_entry)
        history = history[:50]  # Keep last 50 requests
        
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error saving history: {e}")

def show_history():
    try:
        history_file = "data/history.json"
        if not os.path.exists(history_file):
            messagebox.showinfo("History", "No request history found!")
            return
            
        with open(history_file, "r", encoding="utf-8") as f:
            history = json.load(f)
            
        if not history:
            messagebox.showinfo("History", "No request history found!")
            return
            
        # History Window
        history_window = ctk.CTkToplevel(app)
        history_window.title("📜 Request History")
        history_window.geometry("600x500")
        history_window.resizable(True, True)
        history_window.grab_set()  # Keep window on top
        history_window.focus_set()  # Focus on window
        
        # History List
        history_frame = ctk.CTkScrollableFrame(history_window)
        history_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        for i, req in enumerate(history[:10]):
            card = ctk.CTkFrame(history_frame)
            card.pack(fill="x", pady=5, padx=5)
            
            ctk.CTkLabel(card, text=f"{req['method']} - {req['url'][:50]}...", 
                        font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
            ctk.CTkLabel(card, text=f"Status: {req['status_code']} | Time: {req['response_time']}s", 
                        font=("Arial", 10)).pack(anchor="w", padx=10, pady=(0, 5))
        
    except Exception as e:
        messagebox.showerror("Error", f"Error loading history: {e}")

def show_response_chart():
    try:
        history_file = "data/history.json"
        if not os.path.exists(history_file):
            messagebox.showinfo("Charts", "No data available for charts!")
            return
            
        with open(history_file, "r", encoding="utf-8") as f:
            history = json.load(f)
            
        if len(history) < 2:
            messagebox.showinfo("Charts", "Need at least 2 requests for charts!")
            return
            
        # Chart Window
        chart_window = ctk.CTkToplevel(app)
        chart_window.title("📈 Response Time Chart")
        chart_window.geometry("800x600")
        chart_window.resizable(True, True)
        chart_window.grab_set()  # Keep window on top
        chart_window.focus_set()  # Focus on window
        
        # Prepare data
        recent_history = history[:10]
        times = [req['response_time'] for req in recent_history]
        labels = [f"{req['method']} {i+1}" for i, req in enumerate(recent_history)]
        
        # Create matplotlib chart
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(range(len(times)), times, color=['green' if t < 1 else 'orange' if t < 3 else 'red' for t in times])
        ax.set_xlabel('Recent Requests')
        ax.set_ylabel('Response Time (seconds)')
        ax.set_title('API Response Time Chart')
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45)
        
        # Add value labels
        for bar, time_val in zip(bars, times):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                   f'{time_val}s', ha='center', va='bottom')
        
        plt.tight_layout()
        
        # Embed in tkinter
        canvas = FigureCanvasTkAgg(fig, chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error creating chart: {e}")

def show_dashboard():
    try:
        history_file = "data/history.json"
        if not os.path.exists(history_file):
            messagebox.showinfo("Dashboard", "No data available for dashboard!")
            return
            
        with open(history_file, "r", encoding="utf-8") as f:
            history = json.load(f)
            
        if not history:
            messagebox.showinfo("Dashboard", "No data available for dashboard!")
            return
            
        # Dashboard Window
        dash_window = ctk.CTkToplevel(app)
        dash_window.title("📊 Analytics Dashboard")
        dash_window.geometry("700x500")
        dash_window.resizable(True, True)
        dash_window.grab_set()  # Keep window on top
        dash_window.focus_set()  # Focus on window
        
        # Calculate metrics
        total_requests = len(history)
        successful_requests = sum(1 for req in history if 200 <= req['status_code'] < 300)
        success_rate = (successful_requests / total_requests * 100) if total_requests > 0 else 0
        avg_response_time = sum(req['response_time'] for req in history) / total_requests if total_requests > 0 else 0
        
        # Header
        header_frame = ctk.CTkFrame(dash_window, fg_color=COLORS["primary"], height=60)
        header_frame.pack(pady=10, padx=10, fill="x")
        header_frame.pack_propagate(False)
        
        ctk.CTkLabel(header_frame, text="📊 Analytics Dashboard", 
                    font=("Arial", 20, "bold"), text_color="white").pack(expand=True)
        
        # Metrics Grid
        metrics_frame = ctk.CTkFrame(dash_window)
        metrics_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Row 1
        row1 = ctk.CTkFrame(metrics_frame, fg_color="transparent")
        row1.pack(fill="x", pady=10)
        
        # Total APIs
        total_card = ctk.CTkFrame(row1, fg_color=COLORS["secondary"])
        total_card.pack(side="left", fill="both", expand=True, padx=5)
        
        ctk.CTkLabel(total_card, text="Total APIs", font=("Arial", 14, "bold"), text_color="white").pack(pady=(15, 5))
        ctk.CTkLabel(total_card, text=f"{total_requests}", font=("Arial", 24, "bold"), text_color="white").pack(pady=(0, 15))
        
        # Success Rate
        success_card = ctk.CTkFrame(row1, fg_color=COLORS["success"])
        success_card.pack(side="left", fill="both", expand=True, padx=5)
        
        ctk.CTkLabel(success_card, text="Success Rate", font=("Arial", 14, "bold"), text_color="white").pack(pady=(15, 5))
        ctk.CTkLabel(success_card, text=f"{success_rate:.1f}%", font=("Arial", 24, "bold"), text_color="white").pack(pady=(0, 15))
        
        # Row 2
        row2 = ctk.CTkFrame(metrics_frame, fg_color="transparent")
        row2.pack(fill="x", pady=10)
        
        # Average Time
        avg_card = ctk.CTkFrame(row2, fg_color=COLORS["warning"])
        avg_card.pack(side="left", fill="both", expand=True, padx=5)
        
        ctk.CTkLabel(avg_card, text="Avg Response Time", font=("Arial", 14, "bold"), text_color="white").pack(pady=(15, 5))
        ctk.CTkLabel(avg_card, text=f"{avg_response_time:.2f}s", font=("Arial", 24, "bold"), text_color="white").pack(pady=(0, 15))
        
        # Failed APIs
        failed_card = ctk.CTkFrame(row2, fg_color=COLORS["danger"])
        failed_card.pack(side="left", fill="both", expand=True, padx=5)
        
        ctk.CTkLabel(failed_card, text="Failed APIs", font=("Arial", 14, "bold"), text_color="white").pack(pady=(15, 5))
        ctk.CTkLabel(failed_card, text=f"{total_requests - successful_requests}", font=("Arial", 24, "bold"), text_color="white").pack(pady=(0, 15))
        
        # Summary
        summary_frame = ctk.CTkFrame(dash_window)
        summary_frame.pack(pady=10, padx=10, fill="x")
        
        summary_text = f"Dashboard Summary: {total_requests} total | {success_rate:.1f}% success | {avg_response_time:.2f}s avg time"
        ctk.CTkLabel(summary_frame, text=summary_text, font=("Arial", 12)).pack(pady=10)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error creating dashboard: {e}")

send_btn = ctk.CTkButton(
    primary_row,
    text="🚀 Send Request",
    command=send_request,
    width=120,
    height=45,
    font=("Segoe UI", 13, "bold"),
    fg_color=COLORS["primary"],
    hover_color=COLORS["dark"],
    corner_radius=12
)
send_btn.pack(side="left", padx=5)

clear_btn = ctk.CTkButton(
    primary_row,
    text="🗑️ Clear",
    command=clear_response,
    width=80,
    height=45,
    font=("Segoe UI", 13, "bold"),
    fg_color=COLORS["danger"],
    hover_color="#DC2626",
    corner_radius=12
)
clear_btn.pack(side="left", padx=5)

save_btn = ctk.CTkButton(
    primary_row,
    text="💾 Save",
    command=save_response,
    width=80,
    height=45,
    font=("Segoe UI", 13, "bold"),
    fg_color=COLORS["success"],
    hover_color="#16A34A",
    corner_radius=12
)
save_btn.pack(side="left", padx=5)

# Secondary Actions Row
secondary_row = ctk.CTkFrame(action_section, fg_color="transparent")
secondary_row.pack(pady=5)

history_btn = ctk.CTkButton(
    secondary_row,
    text="📜 History",
    command=show_history,
    width=90,
    height=40,
    font=("Segoe UI", 12, "bold"),
    fg_color=COLORS["secondary"],
    hover_color=COLORS["primary"],
    corner_radius=10
)
history_btn.pack(side="left", padx=3)

chart_btn = ctk.CTkButton(
    secondary_row,
    text="📈 Charts",
    command=show_response_chart,
    width=90,
    height=40,
    font=("Segoe UI", 12, "bold"),
    fg_color=COLORS["warning"],
    hover_color="#D97706",
    corner_radius=10
)
chart_btn.pack(side="left", padx=3)

dash_btn = ctk.CTkButton(
    secondary_row,
    text="📊 Dashboard",
    command=show_dashboard,
    width=100,
    height=40,
    font=("Segoe UI", 12, "bold"),
    fg_color="#8B5CF6",
    hover_color="#7C3AED",
    corner_radius=10
)
dash_btn.pack(side="left", padx=3)

# === RIGHT SIDE - RESPONSE ===
right_frame = ctk.CTkFrame(main_container, fg_color="#E1F5FE")
right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

# === RESPONSE SECTION - SIMPLE AND VISIBLE ===
response_frame = ctk.CTkFrame(right_frame, fg_color="lightgray")
response_frame.pack(pady=10, padx=10, fill="both", expand=True)

ctk.CTkLabel(response_frame, text="📊 API RESPONSE", font=("Arial", 16, "bold")).pack(pady=10)

# Status Info
status_info_frame = ctk.CTkFrame(response_frame, fg_color="white")
status_info_frame.pack(pady=5, padx=10, fill="x")

status_code_label = ctk.CTkLabel(status_info_frame, text="Status: Ready", font=("Arial", 12))
status_code_label.pack(side="left", padx=10, pady=5)

time_label = ctk.CTkLabel(status_info_frame, text="Time: -", font=("Arial", 12))
time_label.pack(side="left", padx=10, pady=5)

size_label = ctk.CTkLabel(status_info_frame, text="Size: -", font=("Arial", 12))
size_label.pack(side="left", padx=10, pady=5)

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

# === API STATUS INDICATOR ===
api_status_frame = ctk.CTkFrame(response_frame, height=40)
api_status_frame.pack(pady=5, padx=10, fill="x")
api_status_frame.pack_propagate(False)

api_status_label = ctk.CTkLabel(api_status_frame, text="⚪ Ready", font=("Arial", 14, "bold"))
api_status_label.pack(expand=True)

# === PROFESSIONAL STATUS BAR ===
status_bar = ctk.CTkFrame(right_frame, fg_color=COLORS["light"], corner_radius=10, height=35)
status_bar.pack(pady=(0, 10), padx=10, fill="x")
status_bar.pack_propagate(False)

status_label = ctk.CTkLabel(status_bar, text="✅ Ready to test APIs", font=("Segoe UI", 11), text_color=COLORS["dark"])
status_label.pack(expand=True)

# === PROFESSIONAL KEYBOARD SHORTCUTS ===
app.bind("<Control-Return>", lambda e: send_request())
app.bind("<F5>", lambda e: send_request())
app.bind("<Control-t>", lambda e: toggle_theme())

# === MAIN LOOP ===
if __name__ == "__main__":
    app.mainloop()