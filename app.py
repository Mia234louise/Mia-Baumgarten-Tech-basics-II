import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Launch the gui
root = tk.Tk()
root.title("Helping Hands!")
screen_width = 600
screen_height = 600
root.minsize(screen_width, screen_height)
root.configure(background="#F0F8FF")

# Set up the background picture
image_file_path = "hands.jpeg"
background_colour = "#F0F8FF"


def set_background(root, image_file_path, background_colour):

    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo, bg=background_colour)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)


# Function to clear the window
def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()


# Functions for the search/lend button
def press_1():
    global questioninp_one, search_label
    user_input = questioninp_one.get().strip()
    if user_input:
        search_result = f"We will search a HelpingHand for: {user_input}"
        search_label.config(text=search_result,
                            fg="#006400")
    else:
        messagebox.showwarning("Warning", "Please select a valid option!")

def press_2():
    global questioninp_one, search_label
    user_input = questioninp_one.get().strip()
    if user_input:
        search_result = f"Thank you for offering a Helping Hand!"
        search_label.config(text=search_result, fg="#006400")
    else:
        messagebox.showwarning("Warning", "Please select a valid option!")


# Code of Conduct
def code_of_conduct():
    clear_widgets(root)
    text_code_of_conduct = tk.Label(text="Code of Conduct",
                                    font="Arial 20 bold"
                                    )
    frame = ttk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Set up the frame for the Code of Conduct
    text_frame = ttk.Frame(frame,
                           borderwidth=2,
                           relief="groove"
                           )
    text_frame.pack(fill=tk.BOTH,
                    expand=True,
                    padx=10,
                    pady=10
                    )

    text_widget = tk.Text(text_frame,
                          wrap="word",
                          font="Arial 12 bold",
                          state="normal",
                          bg="#F0F8FF",
                          bd=0
                          )
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Add the Community Code of Conduct text to the text widget
    code_of_conduct_text = """ Community Code of Conduct

Welcome to the HelpingHands community! Our community is built on principles of trust, collaboration, and mutual respect. To ensure a safe and enjoyable experience for all users, we ask that you adhere to the following Code of Conduct:

1. Respect and Inclusivity: Treat all members of the community with respect and dignity. Discrimination, harassment, hate speech, or any form of abusive behavior will not be tolerated.
2. Safety First: Prioritize safety in all interactions. Be mindful of your surroundings and take necessary precautions when borrowing tools or offering help. If you feel unsafe or encounter any concerning behavior, please report it immediately.
3. Clear Communication: Communicate openly and honestly with other users. Clearly discuss expectations, timelines, and any relevant details before engaging in a transaction or collaboration.
4. Privacy and Confidentiality: Respect the privacy and confidentiality of other users. Do not share personal information without consent, and refrain from disclosing sensitive details about others' projects or situations.
5. Fairness and Transparency: Be fair and transparent in your dealings with others. Honor commitments, provide accurate information about your tools or skills, and disclose any limitations or potential challenges upfront.
6. Feedback and Improvement: Provide constructive feedback to help improve the community. Use the rating and feedback system responsibly to share your experiences and contribute to the overall quality of interactions.
7. Empowerment and Support: Support and empower fellow community members. Offer assistance when possible, share your knowledge and expertise, and foster a culture of collaboration and learning.
8. Adherence to Policies: Follow all guidelines, policies, and terms of service outlined by Helping Hands. Familiarize yourself with our rules and regulations, and abide by them to maintain a positive community environment.
9. Accountability: Take responsibility for your actions and their consequences. If you make a mistake or encounter challenges, communicate openly and work towards resolution in a respectful manner.
    
By using Helping Hands, you agree to abide by this Code of Conduct and uphold the values of our community. Together, we can create a supportive and inclusive environment where everyone feels welcome and valued.

If you have any questions or concerns regarding this Code of Conduct, please contact our support team for assistance.

Thank you for being a part of our community!
    """
    text_widget.insert(tk.END, code_of_conduct_text)

    # Disable text widget to make it read-only
    text_widget.config(state="disabled")

    # Button to go back to MyProfile
    button_my_profile = tk.Button(text="Go back to My Profile!",
                                  command=profile_page,
                                  font="arial 10 bold"
                                  )
    button_my_profile.place(x=80, y=500)

    # Button to close the app
    button_close = tk.Button(text="CLOSE THE APP",
                             command=root.destroy,
                             font="arial 10 bold"
                             )
    button_close.place(x=480, y=550)

    # Button to get back to the homepage
    button_homepage = tk.Button(text="🏠",
                                command=homepage
                                )
    button_homepage.place(x=80, y=550)


# Profile Page
def profile_page():
    clear_widgets(root)
    welcome = tk.Label(text="My Profile",
                       font="Arial 20 bold",
                       fg="black"
                       )
    welcome.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    button_code_of_conduct = tk.Button(text="Code of Conduct",
                                       command=code_of_conduct,
                                       font="Arial 15 bold",
                                       relief=tk.RAISED,
                                       borderwidth=3,
                                       fg="black",
                                       bg="#F0F8FF",
                                       width=20
                                       )
    button_code_of_conduct.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    button_offered_items = tk.Button(text="Your offered items",
                                     command=page_offered_items,
                                     font="Arial 15 bold",
                                     relief=tk.RAISED,
                                     borderwidth=3,
                                     fg="black",
                                     bg="#F0F8FF",
                                     width=20
                                     )
    button_offered_items.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    button_borrowed_items = tk.Button(text="Your borrowed items",
                                      command=page_borrowed_items,
                                      font="Arial 15 bold",
                                      relief=tk.RAISED,
                                      borderwidth=3,
                                      fg="black",
                                      bg="#F0F8FF",
                                      width=20
                                      )
    button_borrowed_items.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button_close = tk.Button(text="CLOSE THE APP",
                             command=root.destroy,
                             font="arial 10 bold"
                             )
    button_close.place(x=480, y=550)

    button_homepage = tk.Button(text="🏠",
                                command=homepage
                                )
    button_homepage.place(x=80, y=550)


# Page to show the offered items
def page_offered_items():
    clear_widgets(root)
    offered_items = tk.Label(text="You have 0 items offered",
                             font="Arial 12 bold",
                             fg="black"
                             )
    offered_items.place(x=50, y=100)

    button_offer = tk.Button(text="Would you like to offer items?",
                             command=offering_help_page,
                             font="Arial 15 bold",
                             relief=tk.RAISED,
                             borderwidth=3,
                             bg="#F0F8FF",
                             fg="black"
                             )
    button_offer.place(x=50, y=150)

    button_close = tk.Button(text="CLOSE THE APP",
                             command=root.destroy,
                             font="arial 10 bold"
                             )
    button_close.place(x=480, y=550)

    button_homepage = tk.Button(text="🏠",
                                command=homepage
                                )
    button_homepage.place(x=80, y=550)

    button_my_profile = tk.Button(text="Go back to My Profile!",
                                  command=profile_page,
                                  font="arial 10 bold"
                                  )
    button_my_profile.place(x=80, y=500)


# Page to show the borrowed items
def page_borrowed_items():
    clear_widgets(root)
    borrowed_items = tk.Label(text="You have 0 items borrowed",
                              font="Arial 12 bold",
                              fg="black",
                              bg="#F0F8FF"
                              )
    borrowed_items.place(x=50, y=100)

    button_borrow = tk.Button(text="Would you like to borrow items?",
                              command=looking_for_help_page,
                              font="Arial 15 bold",
                              relief=tk.RAISED,
                              borderwidth=3,
                              bg="#F0F8FF",
                              fg="black",
                              )
    button_borrow.place(x=50, y=150)

    button_close = tk.Button(text="CLOSE THE APP",
                             command=root.destroy,
                             font="arial 10 bold"
                             )
    button_close.place(x=480, y=550)

    button_homepage = tk.Button(text="🏠",
                                command=homepage
                                )
    button_homepage.place(x=80, y=550)

    button_my_profile = tk.Button(text="Go back to My Profile!",
                                  command=profile_page,
                                  font="arial 10 bold"
                                  )
    button_my_profile.place(x=80, y=500)


# Looking for help page
def looking_for_help_page():
    global questioninp_one, search_label
    clear_widgets(root)

    question_one = tk.Label(text="What do you want to do?",
                            font="Arial 15 bold",
                            fg="#483D8B",
                            bg="#F0F8FF"
                            )
    question_one.place(x=50, y=100)

    options_one = ["Build something", "Mount something", "Repair something", "Paint", "Switch something",
                   "Something else"]
    questioninp_one = tk.StringVar()
    inpquestion_one = tk.OptionMenu(root, questioninp_one, *options_one)
    inpquestion_one.config(font="Arial 15 bold")
    inpquestion_one.place(x=370, y=100)

    question_two = tk.Label(text="Which tools do you need for that?",
                            font="Arial 15 bold",
                            fg="#483D8B",
                            bg="#F0F8FF"
                            )
    question_two.place(x=50, y=150)

    options_two = ["No tools", "Hammer", "Ladder", "Brush", "Saw", "Drill", "Vacuum cleaner", "Something else"]
    questioninp_two = tk.StringVar()
    inpquestion_two = tk.OptionMenu(root, questioninp_two, *options_two)
    inpquestion_two.config(font="Arial 15 bold")
    inpquestion_two.place(x=370, y=150)

    question_three = tk.Label(text="Do you need a helping hand?",
                              font="Arial 15 bold",
                              fg="#483D8B",
                              bg="#F0F8FF"
                              )
    question_three.place(x=50, y=200)

    questioninp_three = tk.StringVar()
    inpquestion_three_yes = tk.Radiobutton(text="Yes",
                                           variable=questioninp_three,
                                           value="Yes",
                                           font="Arial 15 bold"
                                           )
    inpquestion_three_no = tk.Radiobutton(text="No",
                                          variable=questioninp_three,
                                          value="No",
                                          font="Arial 15 bold"
                                          )
    inpquestion_three_yes.place(x=370, y=200)
    inpquestion_three_no.place(x=500, y=200)

    question_four = tk.Label(text="Where is your neighbourhood?",
                             font="Arial 15 bold",
                             fg="#483D8B",
                             bg="#F0F8FF"
                             )
    question_four.place(x=50, y=250)

    # Entry Box
    questioninp_four = tk.StringVar()
    questioninp_four_box = tk.Entry(textvar=questioninp_four,
                                    fg="black",
                                    bg="white"
                                    )
    questioninp_four_box.place(x=370, y=250)

    search = tk.Button(text="Search",
                       command=press_1,
                       font="Arial 28 bold",
                       relief=tk.RAISED,
                       borderwidth=3,
                       bg="#483D8B",
                       fg="black",
                       )
    search.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    search_label = tk.Label(text="",
                            font="Arial 15 bold",
                            fg="#006400",
                            bg="#F0F8FF")
    search_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    button_close = tk.Button(text="CLOSE THE APP",
                             command=root.destroy,
                             font="arial 10 bold"
                             )
    button_close.place(x=480, y=550)

    button_homepage = tk.Button(text="🏠",
                                command=homepage
                                )
    button_homepage.place(x=80, y=550)


# Offering help page
def offering_help_page():
    clear_widgets(root)
    global questioninp_one, search_label

    question_one = tk.Label(text="For what can you lend a helping hand ?",
                            font="Arial 15 bold",
                            fg="#483D8B",
                            bg="#F0F8FF"
                            )
    question_one.place(x=50, y=100)

    options_one = ["Build something", "Mount something", "Repair something", "Paint", "Switch something",
                   "Something else"]
    questioninp_one = tk.StringVar()
    inpquestion_one = tk.OptionMenu(root, questioninp_one, *options_one)
    inpquestion_one.config(font="Arial 15 bold")
    inpquestion_one.place(x=370, y=100)

    question_two = tk.Label(text="What can you lend?",
                            font="Arial 15 bold",
                            fg="#483D8B",
                            bg="#F0F8FF"
                            )
    question_two.place(x=50, y=150)

    options_two = ["No tools", "Hammer", "Ladder", "Brush", "Saw", "Drill", "Vacuum cleaner", "Something else"]
    questioninp_two = tk.StringVar()
    inpquestion_two = tk.OptionMenu(root, questioninp_two, *options_two)
    inpquestion_two.config(font="Arial 15 bold")
    inpquestion_two.place(x=370, y=150)

    question_three = tk.Label(text="Can you lend a helping hand?",
                              font="Arial 15 bold",
                              fg="#483D8B",
                              bg="#F0F8FF"
                              )
    question_three.place(x=50, y=200)

    questioninp_three = tk.StringVar()
    inpquestion_three_yes = tk.Radiobutton(text="Yes",
                                           variable=questioninp_three,
                                           value="Yes",
                                           font="Arial 15 bold"
                                           )
    inpquestion_three_no = tk.Radiobutton(text="No",
                                          variable=questioninp_three,
                                          value="No",
                                          font="Arial 15 bold"
                                          )
    inpquestion_three_yes.place(x=370, y=200)
    inpquestion_three_no.place(x=500,y=200)

    question_four = tk.Label(text='Where is your neighbourhood?',
                             font='Arial 15 bold',
                             fg="#483D8B",
                             bg="#F0F8FF"
                             )
    question_four.place(x=50, y=250)

    questioninp_four = tk.StringVar()
    questioninp_four_box = tk.Entry(textvar=questioninp_four,
                                    fg="black",
                                    bg="white"
                                    )
    questioninp_four_box.place(x=370, y=250)

    lend = tk.Button(text="Lend",
                     command=press_2,
                     font="Arial 28 bold",
                     relief=tk.RAISED,
                     borderwidth=3,
                     bg="#483D8B",
                     fg="black",
                     )
    lend.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    search_label = tk.Label(text="",
                            font="Arial 15 bold",
                            fg="#006400",
                            bg="#F0F8FF")
    search_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    button_close = tk.Button(text="CLOSE THE APP",
                             command=root.destroy,
                             font="arial 10 bold"
                             )
    button_close.place(x=480, y=550)

    button_homepage = tk.Button(text="🏠",
                                command=homepage
                                )
    button_homepage.place(x=80, y=550)


# Homepage
def homepage():
    clear_widgets(root)
    set_background(root, image_file_path, background_colour)
    welcome = tk.Label(text="Welcome to the Helping Hands Community!\nWhat do you want to do?",
                       font="Arial 20 bold",
                       fg="black",
                       bg="#F0F8FF"
                       )
    welcome.place(x=80, y=50)

    looking_for_help_button = tk.Button(text="Looking for help",
                                        command=looking_for_help_page,
                                        font="Arial 15 bold",
                                        relief=tk.RAISED,
                                        borderwidth=3,
                                        fg="black",
                                        bg="#F0F8FF",
                                        width=18
                                        )
    looking_for_help_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    offering_help_button = tk.Button(text="Offering help",
                                     command=offering_help_page,
                                     font="Arial 15 bold",
                                     relief=tk.RAISED,
                                     borderwidth=3,
                                     fg="black",
                                     bg="#F0F8FF",
                                     width=18
                                     )
    offering_help_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    profile_button = tk.Button(text="My Profile",
                               command=profile_page,
                               font="Arial 15 bold",
                               relief=tk.RAISED,
                               borderwidth=3,
                               fg="black",
                               bg="#F0F8FF",
                               width=18
                               )
    profile_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button_close = tk.Button(text="CLOSE THE APP",
                             command=root.destroy,
                             font="arial 10 bold"
                             )
    button_close.place(x=480, y=550)


homepage()

root.mainloop()
