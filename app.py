from flask import Flask,request,render_template,url_for,redirect,flash
import os

import helper_functions
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def root():
	return redirect(url_for('home'))


@app.route('/home',methods=['GET','POST'])
def home():
	error = ""
	if request.method == 'POST':
		long_url = request.form['url'].strip(' ')
		if not long_url: #meaning: if blank
			flash('URL cannot be blank or with spaces')
		else:
			if not helper_functions.is_valid_url(long_url):
				flash("Please enter full URL Address")
			else:
				hash_value = helper_functions.update_new_url_to_db_and_get_short_url(long_url)
				# server_website_link must be specified
				short_url = 'https://url-reduce.herokuapp.com' + url_for('root') + hash_value
				# should show the short_link
				# send it as a variable to UI
				return render_template('display_new_short_url.html',short_url=short_url)
	return render_template('URLReduce.html')

# Its time to make the shorter url a longer_url ;)
@app.route('/<hash_value>')
def url_redirect(hash_value):
	original_website_link = helper_functions.get_long_url_from_hash_value(hash_value)
	if original_website_link is None:
		flash('The link you entered does not exist, Enter a URL to generate a shorter URL')
		return redirect(url_for('home'))
	return redirect(original_website_link)

if __name__ == '__main__':
	app.run(debug=False)