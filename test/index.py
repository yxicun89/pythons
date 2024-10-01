from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html', title='flask home')


@app.route('/sum')
def fn_sum():
    return render_template('sum.html', title='flask sum')


@app.route('/sum', methods=['GET','POST'])
def fn_sum_post():
    numbers = request.form.get('numbers')
    number_list = list(map(int, numbers.split()))
    return render_template('sum.html', title='flask sum', result=str(numbers).replace(" ", "+")+"="+str(sum(number_list)))


if __name__ == "__main__":
    app.run(debug=True)