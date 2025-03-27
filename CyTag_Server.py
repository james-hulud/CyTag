from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def tag_text():
	print("Server running")
	return "<p>hello world</p>"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)

