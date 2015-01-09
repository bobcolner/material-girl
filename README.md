# material-girl

###Flask + Material Design

#####Social blogging app template with on material-design based UI. HTML and JSON backend provide by Flask and SQLAlchemy.

![alt text](http://material-design.storage.googleapis.com/publish/v_2/material_ext_publish/0Bx4BSt6jniD7QTA5cHFBUlV3RTA/materialdesign_goals_language.png, "Material Design")

# Bootstrap the app

1. Python
	* requierments/common.txt
	* requierments/dev.txt
	* requierments/prod.txt
2. NPM
	* bower
		* Polymer
		* Materalizecss
		* jquery
	* grunt
	* coffee-script
3. SQLAlchemy Database
	* SQLite (defult)
	* PostgreSQL
	* MySQL
	* Microsoft SQL Server
	* Oracle
	* Amazon Redshift

# Install javascript dependencies
bower install --save

# Setup Python env
virtualenv venv
source venv/bin/activate
	* deactivate

# Install python dependencies

pip install --upgrade pip

pip install -r requirements/dev.txt

# Prep. DB
./manage.py db init

./manage.py db migrate

./manage.py db upgrade

./manage.py shell

Role.insert_roles()

User.generate_fake(100)

Post.generate_fake(100)

User.add_self_follows()

# export Env Vars
1. export SECRET_KEY = 'crazyhourse secert key for secure sessions & forms'
2. export MAIL_USERNAME = noreply@example.com
3. export MAIL_PASSWORD = mailpa$$wod
4. export FLASK_CONFIG = DevelopmentConfig
5. export FLASKY_ADMIN = admin@example.com

# run server
#### ./manage.py runserver -h 0.0.0.0

#Apendex:
### CSS naming convention

.u-utilityName {}

.ComponentName {}

.ComponentName--modifierName {}

.ComponentName-descendant {}

.ComponentName-descendant--modifierName {}

.ComponentName.is-stateOfComponent {}

### Docker 
docker run -p 5000:5000 -it --rm --name="material-girl" -v ~/app:/app -w /app -e "MAIL_USERNAME=..." -e "MAIL_PASSWORD=..." -e "FLASKY_ADMIN=..." python:2 /bin/bash