from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

class Sample:
  def __init__(self, time, source, value):
    self.time = time
    self.source = source
    self.value = value

# A list of [time, value] pairs
data = []

@app.route('/')
def show_activity():
  return render_template('show_activity.html', data=data)


@app.route('/report')
def add_entry():
  sample = Sample(datetime.datetime.now(), request.args.get('source'), request.args.get('value'))
  data.append(sample)
  return 'Success'

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

