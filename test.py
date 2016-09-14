#!flask/bin/python
import json
import base64
from flask import Flask, jsonify, Response, request

test = Flask(__name__)

def getContent(str):
	return str+"hehe"

@test.route('/img', methods=['POST'])
def get_customerInfo():
    if request.method == 'POST':
        f = request.files['img']
        return f.filename
#        f.save('/var/www/uploads/' + secure_filename(f.filename))
#	with open(imgPath,"rb") as imageFile:

#		imgStr = bytes.decode(base64.b64encode(imageFile.read()))
#
#		if len(imgStr) == 0:
#			abort(404)
#		newImgStr = getContent(imgStr) + '!!!!!'
#		result = len(newImgStr)
#		resp = jsonify({'cust': result})
#		resp.status_code = 200

if __name__ == '__main__':
	test.run(debug=True)	
