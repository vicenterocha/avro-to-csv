# Simple scritp to convert avro files to csv


## Setup

The project uses Python 2.7 and requires pip to be installed

1. Install virtualenv for virtual environment configuration
       
        pip install --user virtualenv
    
        # In some cases only the following command works 
        # see https://stackoverflow.com/questions/31133050/virtualenv-command-not-found
        sudo /usr/bin/easy_install virtualenv 

2. Create a virtual environment

        virtualenv venv --python=python2.7

3. Activate the virtual environment

        source ./venv/bin/activate

4. Install all the dependencies using requirements.txt (no dependencies for now)

        pip install -r requirements.txt


## Run

Don't forget to activate the virtual environment.

1. Run the app:

        cd src
        python main.py <input avro file> <output csv file name>

2. To deactivate the virtual environment:
    
        deactivate
    
    
## Tests

Make sure you run the setup first. Then just run the tests with
    
    python -m unittest discover tests -v


