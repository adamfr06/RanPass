# RanPass v1.1.2

A lightweight password management tool that allows you to generate, store, and retrieve passwords effortlessly. This program is written in Python and includes features for secure password handling and an accessible patch notes viewer.

---

## Features
- **Password Generation:** Automatically generates a random, secure 13-character password and saves it to a file for easy access later.
- **Password Retrieval:** Search for saved passwords by the associated service (e.g., Google, Steam, Bank).
- **Patch Notes Viewer:** View the latest updates and changes made to the program.
- **Looped Functionality:** Allows the user to return to the main menu without restarting the program.

---

## How to Use
1. **Run the Program:**
   Start the program by running the Python script in a terminal or IDE.

2. **Choose an Option:**
   When prompted, select one of the following:
   - `g` to generate a new password.
   - `f` to find and retrieve an existing password.
   - `p` to view the patch notes.

3. **Generate a Password (`g`):**
   - Enter the service name (e.g., Google, Steam, Bank, etc.).
   - The program will generate a secure password and save it as `<service>.txt` in the current directory.

4. **Find a Password (`f`):**
   - Enter the service name to retrieve the associated password.
   - Ensure the file exists in the program's directory.

5. **View Patch Notes (`p`):**
   - Displays a summary of the latest updates to the program.

6. **Exit the Program:**
   - Enter `e` when prompted to quit the program.

---

## Requirements
- Python 3.x
- `random` and `string` libraries (pre-installed in Python)

---

## Version History
### v1.1.2
- Added version number display.
- Improved user experience with more spaced-out lines.
- Enabled looping functionality for continuous use.
- Introduced a patch notes page.
- Improved code efficiency and organization.

---

## Notes
- Generated passwords are saved in plain text files. Use with caution in environments where security is a concern.
- Ensure you provide accurate service names when retrieving passwords to avoid file not found errors.

---

**Made by:** polp7  
**Latest Update:** [t.ly/ytyR](https://t.ly/ytyR)
