from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET']')
def predict(): 
    q = request.args.to_dict()
    if len(q) == 0 or len(q)==1:
        num1 = 0
        num2 = 0
        pred = 0
        pred_dict = {
        'features': {
            'num1': num1,
            'num2': num2
        }, 'prediction': pred
    }
        return jsonify(pred_dict)
    else:
        num1 = float(q["num1"])
        num2 = float(q["num2"])
        if (num1+num2) > 5.8:
            pred2 = 1
        else:
            pred2=0
        pred_dict2 = pred_dict = {
        'features': {
            'num1': num1,
            'num2': num2
        },'prediction': pred2
    }
        return jsonify(pred_dict2)
        

if __name__ == '__main__':
    app.run()
    
