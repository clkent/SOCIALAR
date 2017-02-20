#### 1. Make a virtual environment 
Complete these steps inside the top level of repo 
- Setup a virtual environment: 
  - Depending on where your version of Python 3 is installed you may need to alter the path in the command below
  - ```virtualenv -p /usr/local/bin/python3 venv3``` 
- Activate virtual environment: 
  - ```source venv3/bin/activate``` 
  - command above activates the virtual environment your command line prompt should start with ```(venv3)``` if it worked
  
#### 2. Install depencencies with pip
In the top level of the cloned repo there is a ```requirements.txt``` file  
- Install depedencies from requirements.txt: 
  - pip3 install -r requirements.txt  
  
#### 3. Start server
- cd into the ```social_API``` directory. Should contain the ```manage.py``` file.
- In directory with ```manage.py``` run this command: 
  - ```python manage.py runserver``` 
  - see working endpoint at: [http://localhost:8000/social/geo/](http://localhost:8000/social/geo/)
