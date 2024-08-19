import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Initialize the main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x400")

# Contact storage (will be saved in a JSON file)
contacts = {}

# Load contacts from file
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}

# Save contacts to file
def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

# Add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    else:
        messagebox.showwarning("Error", "Name and Phone are required fields.")

# Update contact list in the listbox
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# View contact details
def view_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        details = contacts[name]
        messagebox.showinfo(name, f"Phone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
    else:
        messagebox.showwarning("Error", "Please select a contact.")

# Search for a contact
def search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone Number:")
    if query:
        results = []
        for name, details in contacts.items():
            if query.lower() in name.lower() or query in details['phone']:
                results.append(f"{name} - {details['phone']}")
        if results:
            search_results = "\n".join(results)
            messagebox.showinfo("Search Results", search_results)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

# Update contact details
def update_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if phone:
            contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            save_contacts()
            update_contact_list()
            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        else:
            messagebox.showwarning("Error", "Phone number is required.")
    else:
        messagebox.showwarning("Error", "Please select a contact to update.")

# Delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        if messagebox.askyesno("Delete", f"Are you sure you want to delete '{name}'?"):
            del contacts[name]
            save_contacts()
            update_contact_list()
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
    else:
        messagebox.showwarning("Error", "Please select a contact to delete.")

# User Interface
# Labels and Entry boxes
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
phone_entry = tk.Entry(root, width=40)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=2, column=1, padx=10, pady=10)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
address_entry = tk.Entry(root, width=40)
address_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=4, column=1, padx=10, pady=10)

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.grid(row=5, column=0, padx=10, pady=10)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=5, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=6, column=0, padx=10, pady=10)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=50, height=10)
contact_list.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Load and display contacts when the application starts
load_contacts()
update_contact_list()

# Run the Tkinter event loop
root.mainloop()
