
# pass_generator_python

## Introduction

Project represents a soltuon API generate random passwords based on user's input
user has to provide the following data : 
- password minimum length
- number of digits in the password
- number of special charachters 
- number of passwords to be generated

## Technologies

   * application is written in Python language using Flask library
   * application is Docker based
   * application has the capapility to run under kubernetes

## Starting the application locally
### prerequisits 
   * having python 3.7 installed locally
   * having pip package manager for python

### To start the application run the below commands
* install dependencies
```bash
  $ pip install --trusted-host pypi.python.org -r app/requirements.txt
```  
* start the app
```bash
  $ python app/app.py 

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```  

## Starting the application using docker
### prerequisits 
   * having docker deamon installed

### To start the application in Docker run the below commands

* Build the image
```bash
docker build -t pass_generator:1.0 app/.
```  


* Run the container locally 

```bash
  $ docker run -i pass_generator:1.0

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000 (Press CTRL+C to quit)
```

## Command Line Testing
* with local app

```bash
curl -X GET  -G 'http://0.0.0.0:5000/passwords' -d 'length=20' -d 'digits_count=3' -d 'special_characters_count=5' -d 'pass_count=6'

["k)v56#0&LK5^*uT5J#4L","*19Y^f8%Ozw%oI0()&eT","F9G$)2U32Da@BX^*I!G#","5O)&2&#45I2UQ47d)$39","4)Z&V09!qU&)4sOQ4p9W","3hOhB8Bau&^@!!y^R3Et"]
```

* with container app

```bash
curl -X GET  -G 'http://172.17.0.2:5000/passwords' -d 'length=20' -d 'digits_count=3' -d 'special_characters_count=5' -d 'pass_count=6'

["%Fg75!@)i5(^*^gQnSi5","v4xj5(e&Ie3$44)#6%O^","7VP@T(#6)P*76!Ty)@SY","x!wq!#Yo91jK@N%3g^MN","*)3KT(8Z67p^%RMkV!aW","sa^4f^577^5JbJ#v(^!j"]
```