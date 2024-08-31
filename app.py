from flask import Flask, jsonify, render_template
app=Flask(__name__)


JOBS =[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'Salary': 'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
  },
  {
    'id':3,
    'title':'Big Data Analyst',
    'location':'Mumbai, India',
    'Salary': 'Rs. 30,00,000'
  },
  {
    'id':4,
    'title':'Software Engineer',
    'location':'Delhi, India',
    'Salary': 'Rs. 40,00,000'
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html',jobs =JOBS)
@app.route("/api/jobs")

def list_jobs():
  return jsonify(JOBS)

if __name__=='__main__':
  app.run(host= '0.0.0.0', port=8080, debug=True)