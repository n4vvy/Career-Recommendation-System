import tkinter as tk
from tkinter import messagebox

# Predefined career profiles
careers = {
    "Software Developer": {
        "skills": {"Programming", "Problem Solving", "Logic"},
        "interests": {"Technology", "Building Applications"},
        "description": (
            "Develops, tests and maintains software applications."
        ),
        "learn": "Python, data structures, algorithms and Git"
    },

    "Data Analyst": {
        "skills": {"Python", "Mathematics", "Analytical Thinking"},
        "interests": {"Data", "Research"},
        "description": (
            "Analyzes data to identify patterns and useful insights."
        ),
        "learn": "Pandas, NumPy, SQL and data visualization"
    },

    "UI/UX Designer": {
        "skills": {"Creativity", "Communication", "Design"},
        "interests": {"Design", "User Experience"},
        "description": (
            "Designs user interfaces and improves digital experiences."
        ),
        "learn": "Figma, wireframing and usability testing"
    },

    "Graphic Designer": {
        "skills": {"Creativity", "Design", "Visual Thinking"},
        "interests": {"Design", "Visual Arts"},
        "description": (
            "Creates visual content for communication and branding."
        ),
        "learn": "Typography, composition and design software"
    },

    "Cybersecurity Analyst": {
        "skills": {"Programming", "Problem Solving", "Networking"},
        "interests": {"Technology", "Security"},
        "description": (
            "Helps protect computer systems and digital information."
        ),
        "learn": "Networking, Linux and security fundamentals"
    },

    "Digital Marketer": {
        "skills": {"Communication", "Creativity", "Analytical Thinking"},
        "interests": {"Marketing", "Content Creation"},
        "description": (
            "Promotes products and services through digital channels."
        ),
        "learn": "SEO, content strategy and campaign analytics"
    }
}

# Available skills and interests
all_skills = sorted({
    skill
    for career in careers.values()
    for skill in career["skills"]
})

all_interests = sorted({
    interest
    for career in careers.values()
    for interest in career["interests"]
})


def calculate_score(user_skills, user_interests, career):
    skill_matches = user_skills & career["skills"]
    interest_matches = user_interests & career["interests"]

    skill_score = (
        len(skill_matches) / len(career["skills"])
    ) * 100

    interest_score = (
        len(interest_matches) / len(career["interests"])
    ) * 100

    final_score = 0.6 * skill_score + 0.4 * interest_score

    return final_score


def recommend_careers():
    name = name_entry.get().strip()

    selected_skills = {
        skill_list.get(i)
        for i in skill_list.curselection()
    }

    selected_interests = {
        interest_list.get(i)
        for i in interest_list.curselection()
    }

    if not name:
        messagebox.showerror(
            "Input Error",
            "Please enter your name."
        )
        return

    if not selected_skills or not selected_interests:
        messagebox.showerror(
            "Input Error",
            "Select at least one skill and one interest."
        )
        return

    results = []

    for title, career in careers.items():
        score = calculate_score(
            selected_skills,
            selected_interests,
            career
        )

        if score > 0:
            results.append((score, title, career))

    results.sort(key=lambda item: item[0], reverse=True)

    if not results:
        messagebox.showinfo(
            "No Matches",
            "No matching careers were found."
        )
        return

    output = f"Career Recommendations for {name}\n\n"

    for score, title, career in results[:3]:
        output += (
            f"{title} - Match Score: {score:.1f}%\n"
            f"{career['description']}\n"
            f"Suggested Learning: {career['learn']}\n\n"
        )

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, output)
    result_box.config(state="disabled")


# Main window
root = tk.Tk()
root.title("Career Recommendation System")
root.geometry("750x720")

tk.Label(
    root,
    text="Career Recommendation System",
    font=("Arial", 18, "bold")
).pack(pady=12)

tk.Label(root, text="Enter Your Name").pack()

name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)

tk.Label(
    root,
    text="Select Your Skills (Multiple Selection)"
).pack(pady=5)

skill_list = tk.Listbox(
    root,
    selectmode=tk.MULTIPLE,
    height=8,
    exportselection=False
)

for skill in all_skills:
    skill_list.insert(tk.END, skill)

skill_list.pack(pady=5)

tk.Label(
    root,
    text="Select Your Interests (Multiple Selection)"
).pack(pady=5)

interest_list = tk.Listbox(
    root,
    selectmode=tk.MULTIPLE,
    height=6,
    exportselection=False
)

for interest in all_interests:
    interest_list.insert(tk.END, interest)

interest_list.pack(pady=5)

tk.Button(
    root,
    text="Recommend Careers",
    command=recommend_careers
).pack(pady=12)

tk.Label(
    root,
    text="Recommended Careers",
    font=("Arial", 12, "bold")
).pack()

result_box = tk.Text(
    root,
    height=12,
    width=82,
    wrap="word"
)

result_box.pack(padx=10, pady=8)
result_box.config(state="disabled")

root.mainloop()
