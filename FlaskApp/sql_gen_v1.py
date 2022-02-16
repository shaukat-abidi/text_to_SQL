from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route("/")
def get_root():
    return render_template('swaggerui.html')

@app.route("/generateSQL", methods=['GET'])
def func_gensql():
    str_question = str(request.args.get('question'))
    raw_sql = 'select * from all_tables'
    resp = {'question': str_question, 'translated_sql': raw_sql, "sql_execution": "sample response"}
    return jsonify(resp)

"""
@app.route('/api/docs')
def get_docs():
    print('/api/docs')
    return render_template('swaggerui.html')

@app.route('/api')
def get_api():
    hello_dict = {'en': 'Hello', 'es': 'Hola'}
    lang = request.args.get('lang')
    return jsonify(hello_dict[lang])
"""

if __name__== '__main__':
    app.run(host='127.0.0.1', port=5000)