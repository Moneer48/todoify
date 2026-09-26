# ToDoify
#### 🔗<ins>Video Demo: https://youtu.be/pOmRGbHebSw
#### 📰<ins>Description:
It is well-known that people are facing time management issues, which may lead to devastating results, like confusion with random notes or even missed deadlines. But with _ToDoify_ everything will be solved.

_ToDoify_ is designed for people who want to enhance their productivity by managing their tasks independently. It is a task management web application that is built with _Flask_ and _SQLite_.

The site features a user-friendly interface where users can easily sign up and log in. Users can add, view, mark as complete or incomplete, delete, and star tasks. They can also choose the time zone during sign-up to view their tasks creation dates in their local region and even change it later if they wish!

#### 💡<ins>Features:

 - *Simplicity and Minimal Design*: This feature is more than important for the users who want simplicity in their lives and minimalism. The color palette picked was unique for such a to-do list web app.

 - *Login and Sign Up*: These two features allow for every user to have their own set of tasks without interfering with others' data. When being logged in, the user can log out and continue their journey by either creating a new account or logging in again with their previously created account!

 - *Add Tasks*: Users can add new tasks by filling out a form containing several inputs like *Title*, *Description*, *Due Date*, and *Due Time*. This lets the users organize their tasks easily based on them.

 - *Mark as Complete and Incomplete*: This feature allows the user to set specific tasks as completed. When applied, the specified tasks are moved to a new table, which is named *Completed Tasks*. This can let the users visualize their achievements and feel disciplined. On the other hand, they can undo that if they wish using the _Mark as Incomplete_ button.

 - *Delete Tasks*: Once the tasks are complete, users can delete tasks by removing them permanently from all the tables. This lessens the chaos in the users' atmosphere and enables them to visualize fewer tasks on the page, which motivates them to be eager to finish more tasks.

 - *View Tasks*: Users can view their tasks in two main tables: One for *pending tasks* and the other for *completed tasks*. This is the best implementation to view data minimally and let the user be excited to accomplish more and more tasks.

 - *Star Tasks*: Users can star their tasks to put them in another third table in other page that displays the starred tasks only. This *Important Tasks* table is crucial for the them to give priority to those important tasks and to trick their minds to finish them as soon as possible.

 - *Change Password*: Your password is leaked? No worries! With the _Change Password_ feature, you can change your password easily. Just type your current password and your new password, then your data is ready to in the safe side.

 - *Account Deletion*: You no longer want to use the account? Just login into the account and hit that _Delete Account_ button, with filling your password into the form and submitting. Note that this is a permanent action!

#### 👷🏻‍♂️<ins>Implementation:
I chose _Flask_ and _SQLite_ since both are effective in such a personal project and they are lightweight and ideal for me as a CS50x student with no previous knowledge in web development. I used _Flask_ to implement all the 14 routes with the right logic and backend that prevents hackers from any interference with required or wrong data. _SQLite_ is used to store the data in the database in two tables: _users_ and _info_. _users_ table stores the id, name, username, hashed password, and the current time zone of each user, where _info_ table stores the id of each task corresponding to each user's id, as well as for each task's title, description, the creation data, the due date and time, the status (Whether the task is completed or not), and whether the task is starred or not.

For the design, I tried, at first, to use https://uiverse.io website because it offers futuristic designs, but when mixing it with _Bootstrap_, things went wrong and messy, so I stayed on _Bootstrap_ for simplicity. I also used icons from _Bootstrap_ and _Freepik_ to minimalize the interface perfectly. All these mentioned implementations are just a tiny drop of the sea of implementations in this whole app.


I also used some implementations from _Finance_ problem set, including the _helper.py_ file only, that I used from it the *login_required* function which allows for each user to be logged in before accessing the specified routes. Additionally, I used the _Validator_ footer just to test the HTML syntax instead of just copying code from _layout.html_ and from the specified _main_ part from the HTML page and pasting them in https://validator.w3.org/#validate_by_input.

#### 🌪️<ins>Challenges:
 - Keeping up with university studies.

 - Preserving my health and wellness after staying for long hours on my laptop.

 - Debugging routes.

 - Managing time zones.

 - Writing two pages using _uiverse_ with _Bootstrap_ together and then switching to _Bootstrap_ alone, which wasted so much time.

 - Implementing the web app's security from hackers.

 - Adapting the website with all screen sizes to have the suitable interface.

 - Doing every single step alone with no peers. But this was good for me to learn how to stay independent, especially in a large project like this!

Despite of all these challenges, everything was okay with time management, being disciplined, and staying patient.

#### 🔮<ins>Future Work:
In the future, I would like to learn _AJAX_ from scratch and in intense and implementing its features in my web application, so that it doesn't need to refresh the page when the user interacts with the website. Also, I may possibly share it online so that everyone can have access to this life-changing masterpiece.

#### ⤵️<ins>Conclusion:
After finishing this project, I can proudly say that I am confident with my coding skills, including _SQL_ queries, _HTML_, _CSS_, _JavaScript_, _Python_, and _JINJA_ syntax and semantics. All these allowed me to learn what sessions and routes are, and allowed me to have a huge information of how websites work and how to handle a real-world project efficiently.

I can now say: **I am proudly a CS50x student!**
