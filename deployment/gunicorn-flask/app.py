from flask import Flask, request, jsonify
import malaya

app = Flask(__name__)

model = malaya.sentiment.transformer(
    model = 'albert', size = 'base', validate = False
)


@app.route('/', methods = ['GET'])
def index():
    strings = [request.args.get('string')] * 50
    r = model.predict_batch(strings, get_proba = True)
    return jsonify('done')


application = app
