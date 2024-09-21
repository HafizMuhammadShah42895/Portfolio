from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for MySQL database and email
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:muhammad%40555@localhost/portfolio'
app.config['SECRET_KEY'] = 'secretkey'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hafizmuhammadshah11@gmail.com'
app.config['MAIL_PASSWORD'] = 'dujz upaw ucpp rbgo'

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Database Model for Contact messages
class ContactMessage(db.Model):
    __tablename__ = 'contact_message'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save message in the database
        new_message = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()

        # Send email
        msg = Message('New Contact Message', sender=email, recipients=['your_email@gmail.com'])
        msg.body = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(msg)

        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
