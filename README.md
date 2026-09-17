# Overview

As a software engineer, I wanted to take the Client & Project Tracker I built
in Module 1 and push it further — turning something that only existed while
the program was running into something that actually persists. I've worked
with MongoDB and React before, but this is my first time using Firebase
Firestore, so for this module I rebuilt the tracker in Python and connected
it to Firestore to learn how it structures and stores data compared to what
I'd used previously.

The program runs from a console menu and lets you add a new client or
project, view all clients and projects currently stored, update a project's
status, and remove a client or project you no longer need. Every one of
those actions reads from or writes to the Firestore database in real time.

I wanted to build this to get hands-on with a new cloud database and see
how its document-based structure compares to relational or other NoSQL
systems I've used before.

[Software Demo Video](https://www.youtube.com/watch?v=UO_tYknMTb0) 

# Cloud Database

I used Firebase Firestore, Google's NoSQL cloud database, to store the
tracker's data. Firestore organizes data into collections and documents
rather than rows and tables, so I created a "clients" collection where each
document represents one client or project, with fields for the client's
name, the project name, and the project's current status.

I connected to Firestore from Python using the firebase-admin library,
authenticating with a Service Account key. That key file is kept out of the
public GitHub repository (via .gitignore) since it grants admin access to
the database.

# Development Environment

I used Visual Studio Code as my code editor and the VS Code terminal to run
and test the program. I wrote the software in Python, and used the
firebase-admin library to connect to and interact with Firestore.

# Useful Websites

- [Firebase Firestore Documentation](https://firebase.google.com/docs/firestore)
- [firebase-admin Python SDK Documentation](https://firebase.google.com/docs/reference/admin/python)
- [Cloud Database using Firestore](https://www.youtube.com/watch?v=v_hR4K4auoQ)
- [What is Firestore](https://www.youtube.com/watch?v=moglAjmwmUQ)


# Future Work

- Add input validation to prevent duplicate or empty client/project entries
- Let the user select a record by number from the displayed list instead of copying the long document ID
