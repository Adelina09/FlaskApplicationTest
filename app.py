from flask import Flask, render_template
from templates import dummyData
from flask_mysqldb import MySQL

app=Flask(__name__)


mysql=MySQL(app)

app.config['MYSQL_HOST']='34.89.88.117'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='SFIA1'

@app.route('/')
@app.route('/Home')

def hello():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM Location")
    mysql.connection.commit()
    rows=cur.fetchall()
    cur.close()
 
    info=[]

    for row in rows:
        info.append(row)
    print(info)

    return render_template("index.html", title='project', info1=info)

def home():
    return render_template("index.html", title='project')

@app.route('/Scope')
def scope():
    return render_template("Scope.html", title='Scope', posts=dummyData.dummyData)

if __name__=='__main__':
    app.run('0.0.0.0',debug=True)