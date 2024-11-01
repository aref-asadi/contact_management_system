import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import re

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        
        # Set up search bar with label and entry box, binds search function on key release
        tk.Label(root, text="Search:").pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        self.search_entry.bind("<KeyRelease>", self.search_contacts)

        # Set up contact list display using Treeview for structured contact details
        self.contact_list = ttk.Treeview(root, columns=("Name", "Phone", "Email"), show="headings")
        self.contact_list.heading("Name", text="Name")
        self.contact_list.heading("Phone", text="Phone")
        self.contact_list.heading("Email", text="Email")
        self.contact_list.pack()

        # Add buttons for functionalities (Add, Edit, Delete, Exit)
        ttk.Button(root, text="Add Contact", command=self.add_contact).pack()
        ttk.Button(root, text="Edit Contact", command=self.edit_contact).pack()
        ttk.Button(root, text="Delete Contact", command=self.delete_contact).pack()
        ttk.Button(root, text="Exit", command=self.exit_program).pack()
        
        # Load contacts from file and display them in the interface
        self.contacts = self.load_contacts()
        self.display_contacts()

        # Apply custom styles to improve UI appearance
        self.apply_styles()

    def apply_styles(self):
        # Define custom styles for buttons and headings
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12))
        style.configure("Treeview.Heading", font=("Helvetica", 14))

    def add_contact(self):
        # Prompt user to input contact details
        name = simpledialog.askstring("Add Contact", "Enter Name:")
        phone = simpledialog.askstring("Add Contact", "Enter Phone:")
        email = simpledialog.askstring("Add Contact", "Enter Email:")

        # Validate input and add contact if valid
        if name and phone and email:
            if not self.is_valid_phone(phone):
                messagebox.showwarning("Invalid Data", "Phone number should contain only digits.")
                return
            if not self.is_valid_email(email):
                messagebox.showwarning("Invalid Data", "Invalid email format.")
                return

            # Add contact to the list and update display
            new_contact = {"name": name, "phone": phone, "email": email}
            self.contacts.append(new_contact)
            self.save_contacts()
            self.display_contacts()
        else:
            messagebox.showwarning("Incomplete Data", "All fields are required!")

    def edit_contact(self):
        # Check if a contact is selected for editing
        selected_item = self.contact_list.selection()
        if not selected_item:
            messagebox.showwarning("Select Contact", "Please select a contact to edit.")
            return

        # Get selected contact's index and details
        index = self.contact_list.index(selected_item)
        contact = self.contacts[index]

        # Prompt user for new contact details with initial values
        new_name = simpledialog.askstring("Edit Contact", "Edit Name:", initialvalue=contact["name"])
        new_phone = simpledialog.askstring("Edit Contact", "Edit Phone:", initialvalue=contact["phone"])
        new_email = simpledialog.askstring("Edit Contact", "Edit Email:", initialvalue=contact["email"])

        # Validate new input and update contact if valid
        if new_name and new_phone and new_email:
            if not self.is_valid_phone(new_phone):
                messagebox.showwarning("Invalid Data", "Phone number should contain only digits.")
                return
            if not self.is_valid_email(new_email):
                messagebox.showwarning("Invalid Data", "Invalid email format.")
                return

            # Update contact details and refresh display
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            self.save_contacts()
            self.display_contacts()
        else:
            messagebox.showwarning("Incomplete Data", "All fields are required!")

    def delete_contact(self):
        # Check if a contact is selected for deletion
        selected_item = self.contact_list.selection()
        if not selected_item:
            messagebox.showwarning("Select Contact", "Please select a contact to delete.")
            return

        # Confirm deletion action with the user
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            # Delete contact from list and refresh display
            index = self.contact_list.index(selected_item)
            del self.contacts[index]
            self.save_contacts()
            self.display_contacts()

    def load_contacts(self):
        # Load contacts from file if exists, otherwise return an empty list
        try:
            with open("contacts.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        # Save all contacts to file in JSON format
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def display_contacts(self):
        # Sort contacts alphabetically by name
        self.contacts = sorted(self.contacts, key=lambda x: x['name'])

        # Clear current display in Treeview
        for item in self.contact_list.get_children():
            self.contact_list.delete(item)

        # Insert each contact into Treeview
        for contact in self.contacts:
            self.contact_list.insert("", "end", values=(contact["name"], contact["phone"], contact["email"]))

    def search_contacts(self, event):
        # Get the search query from the entry
        query = self.search_entry.get().lower()
        
        # Clear current display
        for item in self.contact_list.get_children():
            self.contact_list.delete(item)

        # Display only contacts that match the search query
        for contact in self.contacts:
            if query in contact["name"].lower():
                self.contact_list.insert("", "end", values=(contact["name"], contact["phone"], contact["email"]))

    def exit_program(self):
        # Save contacts and exit program
        self.save_contacts()
        self.root.quit()

    def is_valid_phone(self, phone):
        # Check if phone number contains only digits
        return phone.isdigit()

    def is_valid_email(self, email):
        # Validate email format with regex
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        return re.match(email_regex, email) is not None

if __name__ == "__main__":
    # Create the main application window and run the ContactManager app
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
