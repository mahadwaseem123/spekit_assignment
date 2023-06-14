# Docs Store System

# Setup Steps:

# Update the System
sudo apt-get update

# To get this repository, run the following command inside your git enabled terminal
git clone https://github.com/mahadwaseem123/spekit_assignment.git

# Install pip
sudo apt install python3-pip -y

# Run this command to install dependencies
pip install -r requirements.txt

Once you have downloaded django,Python3 and all dependencies from requirements.txt, go to the cloned repo directory and run the following command
python3 manage.py makemigrations
This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
python3 manage.py migrate

One last step and then our Docs Store App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
python3 manage.py createsuperuser

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our Docs Store App. Start the server by following command
python3 manage.py runserver

Once the server is hosted, head over to http://44.192.130.48:8000/ for the App.



