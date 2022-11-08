from flask import *
import json, time
import scalar

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set ={'Page': 'Home', 'Message': 'Successfully loaded the home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/scale/', methods=['GET'])
def request_page():

    user_query = str(request.args.get('values')) # /scale/?values=0.10/0.2/1/100/2/1/0/1/0/1/0/1/0/1/1/1/0/1

    ndarray = scalar.transform(user_query)





    data_set ={'value_one': f'{ndarray[0][0]}', 'value_two': f'{ndarray[0][1]}', 
                'value_three': f'{ndarray[0][2]}', 'value_four': f'{ndarray[0][3]}', 
                'value_five': f'{ndarray[0][4]}', 'value_six': f'{ndarray[0][5]}', 
                'value_seven': f'{ndarray[0][6]}', 'value_eight': f'{ndarray[0][7]}', 
                'value_nine': f'{ndarray[0][8]}', 'value_ten': f'{ndarray[0][9]}', 
                'value_eleven': f'{ndarray[0][10]}', 'value_twelve': f'{ndarray[0][11]}', 
                'value_thirteen': f'{ndarray[0][12]}', 'value_fourteen': f'{ndarray[0][13]}', 
                'value_fifteen': f'{ndarray[0][14]}', 'value_sixteen': f'{ndarray[0][15]}', 
                'value_seventeen': f'{ndarray[0][16]}', 'value_eighteen': f'{ndarray[0][17]}'}
    

    json_dump = jsonify(data_set)
    json_dump.headers.add('Access-Control-Allow-Origin', '*')

    return json_dump

# if __name__ == '__main__':
#     app.run(port=7777)