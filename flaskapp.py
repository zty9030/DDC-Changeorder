from flask import Flask, request, session, g, redirect, url_for, abort, \
render_template, flash

from tools.model import randomforest

app = Flask(__name__)

RESULT = {'para':{},'res':[]}

@app.route("/")
def index():
    return render_template('index.html',results = RESULT)




@app.route("/analysis",methods=['POST'])
def analysis():
	global RESULT
	RESULT['para'] = dict(zip(request.form.keys(),request.form.values()))
	RESULT['res'] = randomforest(RESULT['para'])
	return redirect(url_for('index'))

@app.route("/clean")
def clean():
	global RESULT
	RESULT = {'para':{},'res':[]}
	return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
