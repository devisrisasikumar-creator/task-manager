from flask import Flask,render_template,request

app = Flask(__name__)

tasks=[]

@app.route('/',methods=['GET','POST'])
def home():

    if request.method=='POST':

        task=request.form.get('task')

        tasks.append(task)

    return render_template('dashboard.html',tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)