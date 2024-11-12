from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def show_time():
    # Get the current time in a more detailed format
    current_time = datetime.now().strftime("%A, %B %d, %Y - %H:%M:%S")
    # Return a more detailed HTML response
    return f"""
    <html>
        <head><title>Current Time</title></head>
        <body>
            <h1>Welcome to My Flask Web Application!</h1>
            <p>The current date and time is:</p>
            <h2>{current_time}</h2>
            <p>Thank you for visiting!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
