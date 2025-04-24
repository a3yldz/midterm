from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def home():
    return "Zeynep Gülce and Atakan Yıldız DEPLOY"

if __name__ == '__main__':
    app.run()
