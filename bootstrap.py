from subprocess import call


# Set up virtual environment for isolation
call(["virtualenv", "-p", "python3", "virtualenv"])

# Install required libraries.
call(["pip3", "install", "-r", "requirements.txt"])
