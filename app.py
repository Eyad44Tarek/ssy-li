from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    pet_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    appointments = Appointment.query.all()
    return render_template('index.html', appointments=appointments)

@app.route('/add', methods=['POST'])
def add():
    client_name = request.form['client_name']
    pet_name = request.form['pet_name']
    date = request.form['date']
    reason = request.form['reason']

    new_appointment = Appointment(client_name=client_name, pet_name=pet_name, date=date, reason=reason)
    db.session.add(new_appointment)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
