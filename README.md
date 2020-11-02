# Blog Website

## By Stacy Weru

## Description

This is a blogging site created for the user to write whatever they desire and share the views on different topics.This website allows one to log in or create their own account and start blogging.Their articles will be viewed by the readers and they (the readers) will be able to vote on that blog and also comment on that or delete malicious comments that they may come across.

The site can be viewed at https://ace-blog.herokuapp.com/ 

## SetUp / Installation Requirements

### Pre-requisites

* python3
* pip
* virtualenv

### Cloning

* In your terminal:

        $git clone https://github.com/StacyWeru/Blog/
        $cd Blog

## Running the Application

* Creating the virtual environment

        $python3 -m venv virtual
        $source virtual/bin/activate
        $curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $python3 -m pip install Flask
        $python3 -m pip install Flask-Bootstrap
        $python3 -m pip install Flask-Script

* To run the application, in your terminal:

        $chmod +x start.sh
        $./start.sh

## Testing the Application

* To run the tests for the class files:

        $python3 manage.py tests

## Technologies Used

* Python3
* Flask

## License

MIT License

## Copyright

Copyright (c) 2020 Stacy Weru
