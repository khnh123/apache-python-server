from flask import Flask, render_template, request, jsonify
import testPlotly

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/reports')
def wob_reports():
    return render_template('reports.html')


@app.route('/testing')
def testing():
    return render_template('testing.html')


@app.route('/testing/random')
def test_random():
    return render_template('/testing/random.html')


@app.route('/testing/test_form')
def test_form():
    return render_template('/testing/test_form.html')


@app.route('/testing/test_form_response', methods=['POST'])
def test_form_response():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return 'Hello %s %s !<br/><br/><a href="/testing/test_form">Back</a>' % (first_name, last_name)


@app.route('/testing/testPlotly')
def test_plotly():
    return render_template('/testing/testPlotly.html')


@app.route('/testing/testPlotly_response')
def test_plotly_response():
    n_points = int(request.args.get('n_points'))
    df = testPlotly.get_data(n_points)
    html_chart = testPlotly.get_plotly_html(df, '# points = ' + str(n_points))
    return jsonify({'html': html_chart})


app.debug = True  # debug mode is on
from werkzeug.debug import DebuggedApplication

app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

if __name__ == '__main__':
    app.run(debug=True)
