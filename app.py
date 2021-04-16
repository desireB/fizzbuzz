# interpreter TBD
# -*- coding: utf-8 -*-

##################################################
## {Description}
##################################################
## {License_info}
##################################################
## Author: Desire BANSE
## Version: 0.9
## Email: desibanse@gmail.com
## Status: devel
##################################################


from flask import Flask
from flask import request


app = Flask(__name__)

"""
This is the landing page
"""
@app.route('/')
def home():
    return 'FizzBuzz for Markforged by Desire BANSE!'

"""
In case there is an issue with the URL
"""
@app.errorhandler(404)
def page_not_found(e):
    return "[ERR]: Please check the URL"

"""
This is our main function that implements the game
"""
@app.route("/fizzbuzz/<number>", methods=['GET'])
def fizzbuzz(number):
    try:
        int_parameter= int(number)
        return (" ".join([
        "{0}{1}".format(
            "Fizz" if int_parameter % 3 == 0 else "",
            "Buzz" if int_parameter % 5 == 0 else ""
        )
        or number
        ]))
    except ValueError:
        return "[ERR]: This not a number"

if __name__ == "__main__":
    app.run(debug=False)
