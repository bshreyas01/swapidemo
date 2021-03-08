from flask import Flask,jsonify,request,render_template,url_for,redirect
import requests,json,sys


app=Flask(__name__)

mcs=dict()

for i in range(1,10):
    url = 'https://swapi.dev/api/people/'     #need to divide url to make search process more dynamic
    r = requests.get(url+str(i))
    data=r.json()
    if(data['name']=='Luke Skywalker' or data['name']=='Leia Organa' or data['name']=='Darth Vader' or data['name']=='R2-D2' or data['name']=='C-3PO') :
        mcs[data['name']]=data

@app.route('/', methods=['GET', 'POST'])
def roo():
    if request.method=='GET':
        return render_template('a.html')
    elif request.method == 'POST':
        if 'click' in request.form:
            return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method == 'POST':
        if 'l' in request.form:
            return (mcs['Luke Skywalker'])
        elif 'le' in request.form:
            return (mcs['Leia Organa'])
        elif 'r2' in request.form:
            return (mcs['R2-D2'])
        elif 'da' in request.form:
            return (mcs['Darth Vader'])
        elif 'c3' in request.form:
            return (mcs['C-3PO'])

if __name__ == "__main__":
    app.run(debug=True)