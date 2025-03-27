from flask import Flask

app = Flask(__name__)


@app.route('/')
def tag_text():
	print("Server running")
	return 'hello'

if __name__ == '__main__':
	app.run()

