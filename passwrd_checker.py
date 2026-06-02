import tkinter as tk
from tkinter import ttk
import math
import re

class PasswordStrengthChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Strength Checker")
        self.root.geometry("520x620")
        self.root.resizable(False, False)
        
        # Variables
        self.password_var = tk.StringVar()
        self.show_password = tk.BooleanVar(value=False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="🔐 Password Strength Checker", 
                        font=("Helvetica", 18, "bold"), fg="#4f46e5")
        title.pack(pady=20)
        
        subtitle = tk.Label(self.root, text="Create unbreakable passwords", 
                           font=("Helvetica", 11), fg="gray")
        subtitle.pack(pady=(0, 20))
        
        # Password Input
        tk.Label(self.root, text="Enter Password:", font=("Helvetica", 11, "bold")).pack(anchor="w", padx=40)
        
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=8, padx=40, fill="x")
        
        self.password_entry = tk.Entry(input_frame, textvariable=self.password_var, 
                                      font=("Helvetica", 14), show="*", width=40)
        self.password_entry.pack(side="left", fill="x", expand=True, ipady=8)
        
        self.toggle_btn = tk.Button(input_frame, text="👁️", width=3, 
                                   command=self.toggle_visibility)
        self.toggle_btn.pack(side="right", padx=(5, 0))
        
        # Check Button
        self.check_btn = tk.Button(self.root, text="Check Strength", font=("Helvetica", 12, "bold"),
                                  bg="#4f46e5", fg="white", height=2,
                                  command=self.check_password)
        self.check_btn.pack(pady=15, padx=40, fill="x")
        
        # Result Frame
        self.result_frame = tk.Frame(self.root)
        
        # Strength Meter
        tk.Label(self.result_frame, text="Strength:", font=("Helvetica", 11, "bold")).pack(anchor="w", padx=40)
        
        self.strength_var = tk.StringVar(value="Enter a password")
        self.strength_label = tk.Label(self.result_frame, textvariable=self.strength_var, 
                                      font=("Helvetica", 16, "bold"))
        self.strength_label.pack(pady=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.result_frame, length=420, mode='determinate')
        self.progress.pack(pady=10, padx=40)
        
        # Entropy
        self.entropy_label = tk.Label(self.result_frame, text="", font=("Helvetica", 10), fg="gray")
        self.entropy_label.pack(pady=5)
        
        # Criteria
        tk.Label(self.result_frame, text="Requirements:", font=("Helvetica", 11, "bold")).pack(anchor="w", padx=40, pady=(20, 8))
        
        self.criteria = {}
        criteria_list = [
            ("length", "At least 12 characters"),
            ("upper", "Contains uppercase letter (A-Z)"),
            ("lower", "Contains lowercase letter (a-z)"),
            ("digit", "Contains number (0-9)"),
            ("special", "Contains special character (!@#$...)")
        ]
        
        for key, text in criteria_list:
            frame = tk.Frame(self.result_frame)
            frame.pack(anchor="w", padx=40, pady=4)
            
            check = tk.Label(frame, text="○", font=("Helvetica", 14), width=2, fg="gray")
            check.pack(side="left")
            
            label = tk.Label(frame, text=text, font=("Helvetica", 10))
            label.pack(side="left")
            
            self.criteria[key] = {"check": check, "label": label}
        
        # Feedback
        self.feedback_text = tk.Text(self.result_frame, height=5, wrap="word", 
                                    font=("Helvetica", 10), bg="#f8fafc", relief="flat")
        self.feedback_text.pack(pady=20, padx=40, fill="x")
        
        self.result_frame.pack(fill="both", expand=True)
        
        # Bind real-time update
        self.password_var.trace("w", lambda *args: self.live_check())
        
    def toggle_visibility(self):
        if self.show_password.get():
            self.password_entry.config(show="*")
            self.toggle_btn.config(text="👁️")
            self.show_password.set(False)
        else:
            self.password_entry.config(show="")
            self.toggle_btn.config(text="🙈")
            self.show_password.set(True)
    
    def calculate_entropy(self, password):
        charset_size = 0
        if re.search(r'[a-z]', password): charset_size += 26
        if re.search(r'[A-Z]', password): charset_size += 26
        if re.search(r'\d', password): charset_size += 10
        if re.search(r'[^A-Za-z0-9]', password): charset_size += 32
        
        if charset_size == 0:
            return 0
        return round(len(password) * math.log2(charset_size))
    
    def get_strength(self, score):
        if score < 40:
            return "Very Weak", "#ef4444", 25
        elif score < 60:
            return "Weak", "#f59e0b", 45
        elif score < 80:
            return "Medium", "#eab308", 70
        elif score < 100:
            return "Strong", "#84cc16", 90
        else:
            return "Very Strong", "#22c55e", 100
    
    def live_check(self):
        if len(self.password_var.get()) > 3:
            self.check_password()
    
    def check_password(self):
        password = self.password_var.get().strip()
        
        if not password:
            self.strength_var.set("Enter a password")
            self.progress['value'] = 0
            return
        
        # Checks
        has_length = len(password) >= 12
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[^A-Za-z0-9]', password))
        
        # Update criteria
        self.criteria["length"]["check"].config(text="✓" if has_length else "○", 
                                              fg="#22c55e" if has_length else "gray")
        self.criteria["upper"]["check"].config(text="✓" if has_upper else "○", 
                                              fg="#22c55e" if has_upper else "gray")
        self.criteria["lower"]["check"].config(text="✓" if has_lower else "○", 
                                              fg="#22c55e" if has_lower else "gray")
        self.criteria["digit"]["check"].config(text="✓" if has_digit else "○", 
                                              fg="#22c55e" if has_digit else "gray")
        self.criteria["special"]["check"].config(text="✓" if has_special else "○", 
                                                fg="#22c55e" if has_special else "gray")
        
        # Calculate score
        entropy = self.calculate_entropy(password)
        score = 0
        score += 25 if has_length else 0
        score += 15 if has_upper else 0
        score += 15 if has_lower else 0
        score += 15 if has_digit else 0
        score += 20 if has_special else 0
        score += min(entropy // 2, 25)
        
        strength_text, color, progress_value = self.get_strength(score)
        
        # Update UI
        self.strength_var.set(strength_text)
        self.strength_label.config(fg=color)
        self.progress['value'] = progress_value
        self.progress.configure(style=f"{strength_text.replace(' ', '')}.Horizontal.TProgressbar")
        
        self.entropy_label.config(text=f"Entropy: {entropy} bits")
        
        # Feedback
        feedback = ""
        if strength_text == "Very Strong":
            feedback = "Excellent password! Very high resistance to brute-force attacks."
        elif strength_text == "Strong":
            feedback = "Strong password. Well done!"
        elif strength_text == "Medium":
            feedback = "Decent password, but consider making it longer or adding more variety."
        else:
            feedback = "Weak password. Please use at least 12 characters with mixed types."
        
        self.feedback_text.delete(1.0, tk.END)
        self.feedback_text.insert(tk.END, feedback)
        
    def run(self):
        # Configure progress bar colors
        style = ttk.Style()
        style.theme_use('default')
        
        colors = ["#ef4444", "#f59e0b", "#eab308", "#84cc16", "#22c55e"]
        names = ["VeryWeak", "Weak", "Medium", "Strong", "VeryStrong"]
        
        for i, color in enumerate(colors):
            style.configure(f"{names[i]}.Horizontal.TProgressbar", 
                          background=color, troughcolor="#e5e7eb")
        
        self.root.mainloop()


# Run the application
if __name__ == "__main__":
    app = PasswordStrengthChecker()
    app.run()