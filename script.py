import os
import subprocess

def get_scripts(script_dir):
    """Load and return all the .py, .bat, .sh, .js, .rb, .ps1 scripts from the given directory."""
    try:
        scripts = [f for f in os.listdir(script_dir) if f.endswith(('.py', '.bat', '.sh', '.js', '.rb', '.ps1'))]
        return scripts
    except FileNotFoundError:
        print(f"Error: The directory {script_dir} was not found.")
        return []

def run_script(script_path):
    """Run the selected script based on its file extension."""
    try:
        if script_path.endswith('.py'):
            subprocess.run(["python", script_path], shell=True)
        elif script_path.endswith('.bat'):
            subprocess.run([script_path], shell=True)
        elif script_path.endswith('.sh'):
            subprocess.run(["bash", script_path], shell=True)
        elif script_path.endswith('.js'):
            subprocess.run(["node", script_path], shell=True)
        elif script_path.endswith('.rb'):
            subprocess.run(["ruby", script_path], shell=True)
        elif script_path.endswith('.ps1'):
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], shell=True)
        else:
            print(f"Unsupported script type for {script_path}")
    except Exception as e:
        print(f"Error: Failed to run script {script_path}. Details: {e}")

def display_menu(scripts, script_dir):
    """Display the available scripts with their corresponding numbers."""
    print("\n=== Script Launcher ===")
    print(f"Current Directory: {script_dir}")
    for idx, script in enumerate(scripts):
        print(f"{idx + 1}. {script}")
    print(f"{len(scripts) + 1}. Change Directory")
    print(f"{len(scripts) + 2}. Exit")

def get_user_choice(scripts):
    """Get the user input for selecting a script or exiting."""
    choice = input("\nEnter the number of the script to run (or 'q' to quit): ")
    
    if choice.lower() == 'q':  # Quit the launcher
        return 'Exit'
    
    if choice.isdigit() and 1 <= int(choice) <= len(scripts):
        return scripts[int(choice) - 1]
    
    if choice == str(len(scripts) + 1):  # Change directory option
        return 'Change Directory'
    
    print("Invalid selection. Please choose a valid number or 'q' to quit.")
    return None

def get_new_directory():
    """Prompt user to input a new directory."""
    new_dir = input("\nEnter the new directory path: ")
    return new_dir

def main():
    current_directory = r"C:\Users\Guests"  # Default directory set to C:\Users\Guests

    while True:
        scripts = get_scripts(current_directory)
        if not scripts:
            print("No scripts found in the current directory. Please add some scripts.")
            break
        
        display_menu(scripts, current_directory)
        selected_option = get_user_choice(scripts)
        
        if selected_option == 'Exit':
            print("👋 Goodbye!")
            break
        
        if selected_option == 'Change Directory':
            new_directory = get_new_directory()
            if os.path.isdir(new_directory):  # Validate the directory
                current_directory = new_directory
                print(f"Directory changed to: {current_directory}")
            else:
                print(f"Invalid directory: {new_directory}. Please try again.")
        
        elif selected_option:  # Run selected script
            full_path = os.path.join(current_directory, selected_option)
            run_script(full_path)

if __name__ == "__main__":
    main()
