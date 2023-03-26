from flask import Flask
import tensorflow as tf 

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    return'Training completed successfully'

if __name__ == '__main__':
    app.run()

