from flask import Flask,render_template, request
app = Flask(__name__)


weights = [0.6,0.2,0.1,0.1]
who_registered_scores ={
		"parent" : 10,
		"student" : 5.75,
		"someone_else" : 0
}

city_tier_scores ={
		"t1" : 6.48,
		"t2" : 7.05,
		"t3" : 10
}

school_board_scores ={
		"cbse" : 9.12,
		"icse" : 8.56,
		"state_board" : 7.26,
		"others" : 10
}

accual_school_fee_scores ={
		"under_10" : 3.28,
		"10_20" : 4.85,
		"20_30" : 4.78,
		"30_40" : 3.95,
		"40_60" : 4.55,
		"60_80" : 7.69,
		"80_100" : 8.21,
		"100_1000" : 10,
		"none" : 4.83
}

@app.route("/")
def index():
	return render_template('app.html')

@app.route('/send',methods=['POST'])
def send(sum = sum):
    if request.method == 'POST':
        who_registered = request.form['who_registered']
        city_tier = request.form['city_tier']
        school_board = request.form['school_board']
        accual_school_fee = request.form['accual_school_fee']

        # if operations == 'add':
        #     sum = float(firstNumber) + float(secondNumber)
        #     return render_template('app.html' , sum = sum)
        # elif operations == 'subtract':
        #     sum = float(firstNumber) - float(secondNumber)
        #     return render_template('app.html' , sum = sum)
        # elif operations == 'multiply':
        #     sum = float(firstNumber) * float(secondNumber)
        #     return render_template('app.html' , sum = sum)
        # elif operations == 'divide':
        #     sum = float(firstNumber) / float(secondNumber)
        #     return render_template('app.html' , sum = sum)
        # else:
            # return render_template('app.html')

        sum = weights[0]* who_registered_scores[who_registered] + weights[2]* city_tier_scores[city_tier] + weights[3]* school_board_scores[school_board] + weights[1]* accual_school_fee_scores[accual_school_fee]

        return render_template('app.html' , sum = sum, reg = who_registered, city = city_tier, board = school_board, fee = accual_school_fee)

if __name__ == '__main__':
	app.run()