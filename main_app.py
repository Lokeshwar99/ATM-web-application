
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to calculate withdrawal
def calculate_withdrawal(amount):
    notes = [1000, 500, 200, 100, 50]
    coins = [20, 10, 5, 2, 1]
    result = {}

    # Calculate notes
    for note in notes:
        if amount >= note:
            count = amount // note
            amount -= count * note
            result[note] = count

    # Calculate coins
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            amount = int(request.form['amount'])
            if amount <= 0:
                error = "Please enter a positive amount."
                return render_template('index.html', error=error)
            
            result = calculate_withdrawal(amount)
            return render_template('index.html', result=result, amount=amount)
        except ValueError:
            error = "Invalid input. Please enter a numerical value."
            return render_template('index.html', error=error)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
