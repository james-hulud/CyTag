import json
from flask import Flask, request, Response, jsonify
from .CyTag import process
import pandas as pd
import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def tag_text():
	"""Tags the input data using CyTag and returns in CSV format."""
	try:
		data = request.get_json()
		if not data or "text" not in data:
			return jsonify({"status": "error", "message": "Invalid JSON data."}), 400

		text_data = data["text"]

		if not text_data:
			return jsonify({"status": "error", "message": "Text data is empty."}), 400

		# Executes tagging with CyTag and returns result as a string with tab separated columns
		tagged_text = process(text_data)
		df = pd.read_csv(io.StringIO(tagged_text), sep='\t', header=None)
		csv_out = df.to_csv(index=False)
		return Response(csv_out, mimetype="text/csv")
	except Exception as e:
		print(f"Could not tag text data with CyTag: {e}")
		return jsonify({"status": "error", "message": e}), 400


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

