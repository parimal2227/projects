from flask import Flask, render_template, url_for, flash, redirect
from forms import PredictionForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9b9ab03473d5733c41b5e88d22cca1df'


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='about page')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictionForm()
    if form.validate_on_submit():
        flash(f'Predicted House Price for given data is {form.crim.data}!', 'success')
        return redirect(url_for('predict'))
    return render_template('predict.html', title='Predict', form=form)


if __name__ == '__main__':
    app.run(debug=True)
