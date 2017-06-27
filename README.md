### Farmer's Market Challenge
This is a simple calculator to determine which special promotions should apply to a given basket of items, and returning the total.

# How to start
Clone down the project, then cd into the project directory

To calculate the total for a different basket, open the file _register.py_ and change the value of the basket variable on line 87 to contain a list of items you'd like to test.

# How to run the program
First, ensure you have docker installed. Then, to build the docker image, run the following command in the terminal of the project directory:
`$ docker build -t register .`
To run the docker image, enter:
`$ docker run register`

If you have python 2.7 installed, simply running `$ python register.py` should work as well
