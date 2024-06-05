from flask import Flask, render_template


#app = Flask(__name__)
app = Flask(__name__, template_folder='')

@app.route('/')
def index():
    return render_template('index.html')


# run the application
if __name__ == "__main__":  
    app.run(host="localhost", debug=True)
