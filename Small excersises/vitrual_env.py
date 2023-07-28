# first create a virtual environment:
# python -m venv test_venv

# Activate It
# test_venv\Scripts\activate


'''
PowerShell bug “execution of scripts is disabled on this system.”

If you are on Windows here is what you have to follow:
Press the [windows] button and then type PowerShell.
Run as Adiministrator
Copy and Paste the following command and hit [Enter]
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
Type Y and hit [Enter]
Rerun the command and type A hit [Enter]
Close the powershell and try again
'''


# Install Packages Into It
# python -m pip install pandas

# freeze to file
# pip freeze > requirements.txt

#Deactivate It
# deactivate