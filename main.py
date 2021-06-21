from flask import Flask, request,send_file
import json
import proxy_con
import colorize
import random
app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def home():
	rand_name = str(random.randint(1000000000,100000000000))+".jpg"
	print(request.url)
	proxy_con.proxy_get_image(request.url,rand_name)
	colorize.image_colorization(rand_name)
	return send_file("static/out/"+rand_name, mimetype='image/gif')

app.run(debug=True, port=80) 
