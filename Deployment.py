from flask import Flask, request, make_response

app = Flask(__name__)  # reference this file


@app.route('/set')
def set_success():
    resp = make_response('setting cookie')
    resp.set_cookie('Dataframe', 'Pandas')
    return resp


@app.route('/get')
def get_success():
    Dataframe = request.cookies.get('Dataframe')
    return 'The Dataframe is: ' + Dataframe

if __name__ == '__main__':
    app.run(debug=True)
