from flask import Flask, render_template, flash, request
from wtforms import Form, IntegerField, validators, StringField
from score_donor import score


# App config.

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    age = IntegerField('Age:', validators=[validators.required()])
    #workclass = StringField('Work Class:', validators=[])
    #education = StringField('Education:', validators=[])
    #maritalstatus = StringField('Marital Status:', validators=[])
    hoursinlast6months = IntegerField('Hours in Last 6 Hours:', validators=[])
    #occupation = StringField('Marital Status:', validators=[])
    hoursperweek = IntegerField('Hours Per Week:', validators=[validators.required()])
    #inc = StringField('Income:', validators=[])
    #paymentmethod = StringField('Payment Method:', validators=[])

@app.route("/", methods=['GET', 'POST'])

def func():
    form = ReusableForm(request.form)
    try:
        if request.method == 'POST':
            age = request.form['age']
            #inc = request.form['inc']
            #workclass = request.form['workclass']
            #education = request.form['education']
            #maritalstatus = request.form['maritalstatus']
            hoursinlast6months = request.form['hoursinlast6months']
            hoursperweek = request.form['hoursperweek']
            #paymentmethod = request.form['paymentmethod']
            #print("Age - " +age)
            if form.validate():
                # Save the comment here.
                print("")
            else:
                flash('All the form fields are required. ')
            #Save the comment here.
            res = score(age, hoursinlast6months, hoursperweek)
            #print(res)
            flash("Predicted Donation Range - "+res)
            #print("Predicted Donation Range - "+res)

    except Exception as e:
        #print("Exception - " + str(e))
        flash("Exception - " + str(e))
        with open("LOG.txt","w") as f:
            f.write(str(e))

    return render_template('New.html', form=form)

if __name__ == "__main__":
    app.run()
