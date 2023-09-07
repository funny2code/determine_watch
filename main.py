from flask import *

app = Flask(__name__)

@app.route("/")
def questions():
    return render_template('index.html')

@app.route("/chooser", methods=['POST'])
def choose():
    threshold = 460
    watchname = request.form.get("watchname")
    raw_desire = float(request.form.get("raw_desire"))
    raw_use = float(request.form.get("raw_use"))
    raw_quality = float(request.form.get("raw_quality"))
    raw_collection = float(request.form.get("raw_collection"))
    raw_value = float(request.form.get("raw_value"))
    
    adjusted_desire = raw_desire*2
    adjusted_use = raw_use*1.5
    adjusted_quality = raw_quality*1
    adjusted_collection = raw_collection*0.75
    adjusted_value = raw_value*0.5

    total_raw = raw_value+raw_collection+raw_quality+raw_use+raw_desire
    total_adjusted = adjusted_desire+adjusted_use+adjusted_quality+adjusted_collection+adjusted_value

    res = ""
    flag = ""
    if total_adjusted >= threshold:
        res = f"You should buy {watchname}"
        flag = "blue"
    else:
        res = f"Do not buy {watchname}"
        flag = "red"
    
    data = {
        'response': res,
        'flag': flag
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = False, host='127.0.0.1', port=5000)