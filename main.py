from send import mail
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def mymail():
	if request.method == 'POST':
		to_email = request.form['tosend']
		subject = request.form['subject']
		content = request.form['content']
		mail(to_email,subject,content)
		return render_template('success.html')
	return render_template('mailer.html')

if __name__=="__main__":
	app.run(debug=True)