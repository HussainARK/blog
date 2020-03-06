from tkinter import *
from tkinter import messagebox
from pathlib import Path

import os

program_title = "Jekyll Post Creator"

root = Tk()
root.title(program_title)
root.geometry("500x550")

# Functions

try:

    def submit():
        post_name = post_name_entry.get()
        post_date_created = date_entry.get()
        post_title = title_entry.get()
        post_author = author_entry.get()
        post_content = content_text.get("1.0", "end-1c")
        post_layout = layout_entry.get()

        posts_folder = Path("./_posts")

        if post_name and post_date_created and post_title and post_author and post_content and post_layout:
            os.system(
                f"cd _posts && ( echo --- && echo title: {post_title} && echo author: {post_author} && echo layout: {post_layout} && echo --- && echo {post_content} ) > {post_date_created}-{post_name}.md")

            # *Seperator*

            file = ""

            # *Seperator*

            if posts_folder.glob(f"{post_date_created}-{post_name}.md"):
                callback_label = Label(
                    root, text="The Post is created Successfuly!")
            else:
                callback_label = Label(
                    root, text="There's an Error Creating the Post!")

            # *Seperator*

            callback_label.pack()
        else:
            messagebox.showwarning(program_title,
                                   "Please fill all Entries.")

    program_header = Label(
        root, text=f"Welcome to the {program_title} by HussainARK").pack(pady=10)

    post_name_entry_label = Label(
        root, text="Post Name (Seperate multiple words with -): ").pack()
    post_name_entry = Entry(root)
    post_name_entry.pack(pady=10)

    date_entry_label = Label(root, text="Date, Example(2020-01-01): ").pack()
    date_entry = Entry(root)
    date_entry.pack(pady=10)

    title_entry_label = Label(root, text="Title: ").pack()
    title_entry = Entry(root)
    title_entry.pack(pady=10)

    author_entry_label = Label(root, text="Author: ").pack()
    author_entry = Entry(root)
    author_entry.pack(pady=10)

    content_text_label = Label(root, text="Content: ").pack()
    content_text = Text(root, width=40, height=4)
    content_text.pack(pady=10)

    layout_entry_label = Label(root, text="Layout: ").pack()
    layout_entry = Entry(root)
    layout_entry.pack(pady=10)

    submit_button = Button(root, text="Submit Post",
                           command=submit, padx=5, pady=10).pack(pady=1)

    root.mainloop()
except:
    messagebox.showerror(program_title, "Error!")
