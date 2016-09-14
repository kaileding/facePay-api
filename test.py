#!flask/bin/python
import json
import base64
from flask import Flask, jsonify

test = Flask(__name__)

@test.route('/', methods=['GET'])
#@test.route('/facePay/api/v1.0/imgPath', methods = ['GET'])
def get_customerInfo():
	with open('img.jpg',"rb") as imageFile:
		imgStr = bytes.decode(base64.b64encode(imageFile.read()))

		if len(imgStr) == 0:
			abort(404)
		newImgStr = imgStr + '!!!!!'
		result = len(newImgStr)
		#return "hehe"
		return jsonify({'customer': result})

if __name__ == '__main__':
	test.run(debug=True)	
