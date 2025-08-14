from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data for the booking table
bookings = [
    {"id": 1, "name": "John Doe", "status": "Pending"},
    {"id": 2, "name": "Jane Smith", "status": "Pending"}
]

@app.route('/')
def home():
    return render_template('booking.html', bookings=bookings, username="Yogesh")

@app.route('/confirm/<int:id>')
def confirm(id):
    for booking in bookings:
        if booking["id"] == id:
            booking["status"] = "Confirmed"
    return redirect(url_for('home'))

@app.route('/reject/<int:id>')
def reject(id):
    for booking in bookings:
        if booking["id"] == id:
            booking["status"] = "Rejected"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    return redirect(url_for('home'))  # Redirect to home for now, replace with actual logout logic.

if __name__ == "__main__":
    app.run(debug=True)
