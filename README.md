# material-girl

###Flask + Material Design

#####Social blogging app template with on material-design based UI. HTML and JSON backend provide by Flask and SQLAlchemy.

![alt text](http://material-design.storage.googleapis.com/publish/v_2/material_ext_publish/0Bx4BSt6jniD7QTA5cHFBUlV3RTA/materialdesign_goals_language.png "Material Design")

# Bootstrap the app

1. Python [pip install -r]
	* requierments/common.txt
	* requierments/dev.txt
	* requierments/prod.txt
2. NPM [npm install -g]
	* bower
	* grunt
	* coffee-script
3. Bower [bower install --save]
	* Polymer
	* Materalizecss
	* jquery
4. SQLAlchemy Database
	* SQLite (default)
	* PostgreSQL
	* MySQL
	* Microsoft SQL Server
	* Oracle
	* Amazon Redshift

# Clone git-repo
git clone https://github.com/bobcolner/material-girl.git

# Setup Python env
virtualenv venv
source venv/bin/activate
	* deactivate

# Install python dependencies
pip install --upgrade pip && pip install -r requirements/dev.txt

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
1. export SECRET_KEY=secert-key-for-secure-sessions-&-forms
2. export MAIL_USERNAME=noreply@gmail.com
3. export MAIL_PASSWORD=gmailPa$$word
4. export FLASK_CONFIG=development
5. export FLASKY_ADMIN=admin@example.com
6. export FLASKY_MAIL_SENDER="Flasky <flasky@example.com>"
7. export FLASKY_MAIL_SUBJECT_PREFIX=[Flasky]

# Install javascript dependencies

cd app/static/ && bower install --save && cd ../..

# run server
#### ./manage.py runserver -h 0.0.0.0

#Apendex:
### CSS naming convention
[bem-syntax](http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/)

* represents the higher level of an abstraction or component.
.block-name {}

* represents a descendent of .block that helps form .block as a whole.
.block-name__element {}

* represents a different state or version of .block.
.block-name--modifier {}
.block-name__element--modifier {}

* utility class
.u-utility-name {}

### Docker 
docker run -p 5000:5000 -it --rm --name="material-girl" -v ~/app:/app -w /app -e "MAIL_USERNAME=..." -e "MAIL_PASSWORD=..." -e "FLASKY_ADMIN=..." python:2 /bin/bash
 
docker run -p 8888:8888 -it --rm -v ~/app:/app -w /app alankang/anaconda2:latest /bin/bash
ipython notebook --ip 0.0.0.0

### SASS
cd app/assets/static/scss
sass --watch master.scss:../css/master.css
