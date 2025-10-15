import tkinter as tk
from tkinter import messagebox, font

# Tooltip class unchanged (for brevity)
class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 500
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        _id = self.id
        self.id = None
        if _id:
            self.widget.after_cancel(_id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            self.tw,
            text=self.text,
            justify='left',
            background="#333",
            foreground="white",
            relief='solid',
            borderwidth=1,
            wraplength=self.wraplength,
            font=("Segoe UI", 9)
        )
        label.pack(ipadx=5, ipady=3)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()

COURSES = {
    "ai": {
        "beginner": {
            "course": "Intro to Artificial Intelligence",
            "description": "Learn the basics of AI, machine learning concepts, and practical applications.",
            "hours": 6
        },
        "advanced": {
            "course": "Advanced AI Techniques",
            "description": "Deep dive into neural networks, deep learning, and AI algorithms.",
            "hours": 12
        }
    },
    "data science": {
        "beginner": {
            "course": "Intro to Data Analysis",
            "description": "Start with data wrangling, visualization, and basic statistics.",
            "hours": 5
        },
        "advanced": {
            "course": "Data Science with Python",
            "description": "Learn advanced data science techniques using Python libraries.",
            "hours": 11
        }
    },
    "web development": {
        "beginner": {
            "course": "Frontend Basics with HTML/CSS",
            "description": "Build the foundation of web development with HTML, CSS, and JavaScript basics.",
            "hours": 4
        },
        "advanced": {
            "course": "Full-Stack Web Development",
            "description": "Learn frontend and backend development, databases, and deployment.",
            "hours": 10
        }
    },
    "cybersecurity": {
        "beginner": {
            "course": "Cybersecurity Fundamentals",
            "description": "Understand the basics of protecting systems and data.",
            "hours": 5
        },
        "advanced": {
            "course": "Network Security and Penetration Testing",
            "description": "Learn advanced security measures and ethical hacking.",
            "hours": 12
        }
    },
    "mobile apps": {
        "beginner": {
            "course": "Mobile App Development Basics",
            "description": "Get started with building simple mobile apps for Android and iOS.",
            "hours": 6
        },
        "advanced": {
            "course": "Advanced Mobile App Development",
            "description": "Develop complex apps with advanced features and performance optimization.",
            "hours": 13
        }
    },
    "cloud computing": {
        "beginner": {
            "course": "Cloud Computing Essentials",
            "description": "Learn cloud concepts, services, and deployment models.",
            "hours": 5
        },
        "advanced": {
            "course": "Cloud Architecture and DevOps",
            "description": "Master cloud infrastructure, automation, and DevOps tools.",
            "hours": 11
        }
    }
}

class CourseAdvisorApp:
    def __init__(self, root):
        self.root = root
        root.title("Student Course Advisor")
        root.geometry("600x620")
        root.configure(bg="#e6f0ff")  # changed background color

        # Fonts
        self.title_font = font.Font(family="Segoe UI", size=18, weight="bold")
        self.label_font = font.Font(family="Segoe UI", size=11)
        self.btn_font = font.Font(family="Segoe UI", size=12, weight="bold")
        self.course_font = font.Font(family="Segoe UI", size=10, slant="italic")
        self.course_title_font = font.Font(family="Segoe UI", size=11, weight="bold")

        # Title label
        title_label = tk.Label(root, text="Student Course Advisor", bg="#e6f0ff", fg="#2c3e50", font=self.title_font)
        title_label.pack(pady=(20, 10))

        # Interest selection frame
        interests_frame = tk.LabelFrame(root, text="Select Your Interests", bg="white", fg="#34495e",
                                        font=self.label_font, padx=15, pady=10, bd=2, relief="ridge")
        interests_frame.pack(padx=20, pady=10, fill="x")

        self.interests_vars = {}
        interests = ["AI", "Data Science", "Web Development", "Cybersecurity", "Mobile Apps", "Cloud Computing"]
        for i, interest in enumerate(interests):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(interests_frame, text=interest, variable=var,
                                bg="white", fg="#34495e", font=self.label_font, activebackground="#ecf0f1",
                                cursor="hand2", selectcolor="#2980b9")
            cb.grid(row=0, column=i, padx=10, pady=5, sticky="w")
            CreateToolTip(cb, f"Select if interested in {interest} courses")
            self.interests_vars[interest.lower()] = var

        # Study hours frame
        hours_frame = tk.Frame(root, bg="#e6f0ff")
        hours_frame.pack(padx=20, pady=10, fill="x")

        hours_label = tk.Label(hours_frame, text="Available study hours per week:", bg="#e6f0ff", fg="#34495e", font=self.label_font)
        hours_label.grid(row=0, column=0, sticky="w")
        CreateToolTip(hours_label, "How many hours can you dedicate weekly?")

        self.hours_entry = tk.Entry(hours_frame, width=8, font=self.label_font, bd=2, relief="groove")
        self.hours_entry.grid(row=0, column=1, padx=(10, 0))

        # Coding experience frame
        exp_frame = tk.LabelFrame(root, text="Prior Coding Experience?", bg="white", fg="#34495e",
                                  font=self.label_font, padx=15, pady=10, bd=2, relief="ridge")
        exp_frame.pack(padx=20, pady=10, fill="x")

        self.exp_var = tk.StringVar(value="no")
        exp_yes = tk.Radiobutton(exp_frame, text="Yes", variable=self.exp_var, value="yes",
                                 bg="white", fg="#34495e", font=self.label_font, cursor="hand2",
                                 activebackground="#ecf0f1", selectcolor="#2980b9")
        exp_yes.grid(row=0, column=0, padx=15, pady=5)
        CreateToolTip(exp_yes, "Select if you have coding experience")

        exp_no = tk.Radiobutton(exp_frame, text="No", variable=self.exp_var, value="no",
                                bg="white", fg="#34495e", font=self.label_font, cursor="hand2",
                                activebackground="#ecf0f1", selectcolor="#2980b9")
        exp_no.grid(row=0, column=1, padx=15, pady=5)
        CreateToolTip(exp_no, "Select if you do not have coding experience")

        # Recommend button
        recommend_btn = tk.Button(root, text="Get Recommendations", command=self.recommend,
                                  font=self.btn_font, bg="#2980b9", fg="white", activebackground="#1f6391",
                                  relief="raised", bd=3, cursor="hand2")
        recommend_btn.pack(pady=20, ipadx=10, ipady=5)
        CreateToolTip(recommend_btn, "Click to see course recommendations")

        # Results frame
        result_frame = tk.LabelFrame(root, text="Recommended Courses", bg="white", fg="#34495e",
                                     font=self.label_font, padx=15, pady=10, bd=2, relief="ridge")
        result_frame.pack(padx=20, pady=10, fill="both", expand=True)

        scrollbar = tk.Scrollbar(result_frame, orient="vertical")
        self.course_listbox = tk.Listbox(result_frame, font=self.label_font, selectbackground="#2980b9",
                                         activestyle="none", yscrollcommand=scrollbar.set, bd=2, relief="groove")
        scrollbar.config(command=self.course_listbox.yview)
        self.course_listbox.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        result_frame.grid_rowconfigure(0, weight=1)
        result_frame.grid_columnconfigure(0, weight=1)

        self.course_listbox.bind("<<ListboxSelect>>", self.show_course_detail)

        # Course description label
        self.course_desc = tk.Label(root, text="", bg="#e6f0ff", fg="#2c3e50",
                                    font=self.course_font, justify="left", wraplength=550)
        self.course_desc.pack(padx=20, pady=(10, 20))

        # Bottom buttons frame
        bottom_frame = tk.Frame(root, bg="#e6f0ff")
        bottom_frame.pack(pady=10)

        reset_btn = tk.Button(bottom_frame, text="Reset", command=self.reset,
                              font=self.btn_font, bg="#7f8c8d", fg="white", relief="raised", bd=3, cursor="hand2",
                              width=12)
        reset_btn.grid(row=0, column=0, padx=20)

        exit_btn = tk.Button(bottom_frame, text="Exit", command=root.quit,
                             font=self.btn_font, bg="#c0392b", fg="white", relief="raised", bd=3, cursor="hand2",
                             width=12)
        exit_btn.grid(row=0, column=1, padx=20)

    def recommend(self):
        interests = [k for k, v in self.interests_vars.items() if v.get()]
        if not interests:
            messagebox.showwarning("No Interests Selected", "Please select at least one interest.")
            return

        hours_str = self.hours_entry.get().strip()
        if not hours_str.isdigit() or int(hours_str) <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a positive integer for study hours.")
            self.hours_entry.focus()
            return
        hours = int(hours_str)

        experience = self.exp_var.get() == "yes"

        self.recommendations = []
        for interest in interests:
            level = "advanced" if (experience and hours >= 10) else "beginner"
            course_info = COURSES.get(interest, {}).get(level)
            if course_info:
                self.recommendations.append({
                    "interest": interest.title(),
                    "level": level.title(),
                    **course_info
                })

        self.course_listbox.delete(0, tk.END)
        self.course_desc.config(text="")
        if not self.recommendations:
            messagebox.showinfo("No Recommendations", "No courses found for the selected options.")
            return

        for c in self.recommendations:
            # Show course name and interest
            self.course_listbox.insert(tk.END, f"{c['course']} ({c['interest']})")

    def show_course_detail(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            c = self.recommendations[index]
            text = (f"Course: {c['course']}\n"
                    f"Interest Area: {c['interest']}\n"
                    f"Level: {c['level']}\n"
                    f"Recommended Weekly Hours: {c['hours']}\n\n"
                    f"Description:\n{c['description']}")
            self.course_desc.config(text=text)
        else:
            self.course_desc.config(text="")

    def reset(self):
        for var in self.interests_vars.values():
            var.set(False)
        self.hours_entry.delete(0, tk.END)
        self.exp_var.set("no")
        self.course_listbox.delete(0, tk.END)
        self.course_desc.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = CourseAdvisorApp(root)
    root.mainloop()
