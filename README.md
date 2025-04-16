Script Launcher README
Overview
This script launcher allows you to easily navigate and run various types of scripts (Python, Batch, Shell, JavaScript, Ruby, PowerShell) from a directory of your choice. The launcher offers a command-line interface (CLI) that allows users to:

List available scripts in a directory.

Change the directory where the scripts are located.

Run selected scripts with a single key press.

Features
Supports the following script types:

Python (.py)

Batch (.bat)

Shell (.sh)

JavaScript (.js) (Node.js required)

Ruby (.rb)

PowerShell (.ps1)

Allows users to change the script directory at runtime.

Simple CLI interface for easy navigation.

Supports running scripts by selecting a number from a menu.

Exits cleanly when the user decides to stop.

Requirements
Python installed on your system (for running the Python scripts).

Node.js installed (if you plan to run .js scripts).

Ruby installed (if you plan to run .rb scripts).

Bash (for .sh scripts on Linux/macOS systems).

PowerShell (for running .ps1 scripts on Windows).

Default Directory
The script starts by default with the following directory:

makefile
Copy
Edit
C:\Users\Guests
You can change this directory during runtime if your scripts are located elsewhere.

Usage
1. Clone or Download the Script
Clone or download the repository containing the script.

2. Run the Launcher
To run the script launcher, follow these steps:

Open a terminal (or Command Prompt) and navigate to the folder where the script is saved.

Run the script with the following command:

bash
Copy
Edit
python launcher.py
The script will load and display a menu with all available scripts in the current directory.

3. Interact with the Launcher
Once the launcher is running, you will see a menu with options:

Select a Script: Enter the number of the script to run. The selected script will be executed.

Change Directory: If you want to load scripts from a different directory, select the "Change Directory" option. You will be prompted to enter the new directory path.

Exit: If you're done, select the "Exit" option to quit the launcher.

Example Menu:
markdown
Copy
Edit
=== Script Launcher ===
Current Directory: C:\Users\Guests
1. script1.py
2. script2.bat
3. example.sh
4. example.js
5. example.rb
6. example.ps1
7. Change Directory
8. Exit

Enter the number of the script to run (or 'q' to quit):
4. Running Scripts
If you select a Python script (.py), it will be run using the python command.

If you select a Batch script (.bat), it will be executed directly.

Shell scripts (.sh) will be run using bash.

JavaScript (.js) scripts will be executed using node.

Ruby scripts (.rb) will be run using ruby.

PowerShell scripts (.ps1) will be run using powershell.

5. Changing Directory
If you want to use a different directory to load your scripts, you can change the directory at any time by selecting the "Change Directory" option. The script will prompt you for a valid directory path.

Troubleshooting
Invalid Directory
If the script fails to load the scripts from the directory, it will show an error message:

javascript
Copy
Edit
Error: The directory C:\Users\Guests was not found.
Unsupported Script Type
If you attempt to run a script with an unsupported extension, the script will notify you:

pgsql
Copy
Edit
Unsupported script type for script_name.extension
Missing Dependencies
Ensure that you have the necessary interpreters or runtimes installed for each script type:

Python: Python download page

Node.js: Node.js download page

Ruby: Ruby download page

Bash: Bash is available on Linux and macOS by default. For Windows, you can use Git Bash.

PowerShell: PowerShell is pre-installed on Windows.

License
This project is open-source and available under the MIT License.
