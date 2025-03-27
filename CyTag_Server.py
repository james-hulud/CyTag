from flask import Flask, request
from .CyTag import process

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def tag_text():
	print("Server running")
	data = request.get_json()

	tagged_text = process(data["text"])

	return f"<p>{tagged_text}</p>"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)

