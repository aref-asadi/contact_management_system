# Contact Management System

## Overview
This is a Python-based Contact Management System with a graphical user interface (GUI) built using `tkinter`. The application allows users to manage a list of contacts by adding, editing, deleting, and searching for contacts. All contact data is stored in a JSON file for easy retrieval and modification.

## Features
- **Add Contacts**: Add a new contact with name, phone number, and email.
- **Edit Contacts**: Modify an existing contact's information.
- **Delete Contacts**: Remove a contact from the list, with a confirmation prompt.
- **Search Contacts**: Search for contacts by name.
- **Save and Load**: Automatically saves contacts to a JSON file and loads them upon application startup.
- **Exit**: Provides an exit button to save and close the application.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aref-asadi/contact_management_system.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd contactـmanagementـsystem
   ```
3. **Run the Application**:
   Make sure you have Python 3.x installed, then run:
   ```bash
   python contactـmanagementـsystem.py
   ```

## How to Use

1. **Adding a Contact**:
   - Click the "Add Contact" button.
   - Enter the contact’s name, phone, and email in the dialog prompts.
   - The contact will appear in the contact list if all information is valid.

2. **Editing a Contact**:
   - Select a contact from the list.
   - Click the "Edit Contact" button and modify the information as desired.
   - The contact list updates with the new information.

3. **Deleting a Contact**:
   - Select a contact from the list.
   - Click the "Delete Contact" button and confirm deletion.
   - The contact is removed from the list.

4. **Searching for a Contact**:
   - Type a name in the "Search" field at the top.
   - Only contacts matching the search query will display in the list.

5. **Exiting the Application**:
   - Click the "Exit" button to save changes and close the application.

## Data Storage
Contacts are saved in `contacts.json` in JSON format. This file is automatically updated each time you add, edit, or delete a contact, ensuring that all data persists between sessions.

## Code Structure

- **contactـmanagementـsystem.py**: Main application file that contains the GUI, functionalities, and logic for managing contacts.
- **contacts.json**: Data file to store the list of contacts.

## Dependencies
- **Python 3.x**: Ensure Python is installed on your machine.

## Future Enhancements
Potential future improvements could include:
- Exporting contacts to CSV format.
- Adding additional contact fields (address, birthday, etc.).
- Adding group management for organizing contacts.

## License
This project is licensed under the GNU General Public License v3.0.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to update documentation if you add new features.