from flask import Flask, render_template, request
from app.diff_highlighter import DiffHighlighter
from app.aws_services import AWSService

app = Flask(__name__)
diff_highlighter = DiffHighlighter()
aws_service = AWSService()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/diff', methods=['POST'])
def diff_text():
    left_text = request.form['left_text']
    right_text = request.form['right_text']
    line_numbers, highlighted_left, highlighted_right = diff_highlighter.highlight_diff(left_text, right_text)
    return render_template('index.html', left_text=left_text, right_text=right_text,
                           highlighted_left=highlighted_left, highlighted_right=highlighted_right)


if __name__ == '__main__':
    app.run(debug=True)
