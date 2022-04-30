from flask import Flask, jsonify, request
import string
import random

## characters to generate password from

digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

app = Flask(__name__)

@app.route('/passwords', methods=['GET'])
def generate_random_password():
    ## length of password from the user
    length = int(request.args.get('length'))

    ## number of character types

    digits_count = int(request.args.get('digits_count'))
    special_characters_count = int(request.args.get('special_characters_count'))

    characters_count = digits_count + special_characters_count

    ## check the total length with characters sum count
    ## print not valid if the sum is greater than length
    if characters_count > length:
        print("Characters total count is greater than the password length")
        return
    ## number of passwords to be created
    pass_count = int(request.args.get('pass_count'))
    ## initializing the password
    password = []
    password_output = []

    for x in range(pass_count):


        ## picking random digits
        for i in range(digits_count):
            password.append(random.choice(digits))

        ## picking random alphabets
        for i in range(special_characters_count):
            password.append(random.choice(special_characters))

        ## if the total characters count is less than the password length
        ## add random characters to make it equal to the length
        if characters_count < length:
            random.shuffle(characters)
            for i in range(length - characters_count):
                password.append(random.choice(characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
        ## printing the list
        password_output.append("".join(password))
        password.clear()
    ##print("\n".join(password_output))
    return jsonify(password_output), 201

## invoking the app
if __name__ == '__main__':

    # start Flask server
    # Flask's debug mode is unrelated to ptvsd debugger used by Cloud Code
    app.run(debug=False, port=5000, host='0.0.0.0')