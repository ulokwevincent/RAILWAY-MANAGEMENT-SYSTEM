from flask import Flask, render_template,request, redirect
from db import mydb, mycursor


app = Flask(__name__)


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM Train")
    train = mycursor.fetchall()
    return render_template('index.html',train = train)



@app.route('/gotoadmin')
def gotoadmin():
    mycursor.execute("SELECT * FROM Train")
    train = mycursor.fetchall()
    return render_template('adminpage.html',train = train)





@app.route('/addtrain', methods=['GET', 'POST'])
def adddetail():
    if request.method == 'GET':
        return render_template('adddata.html')
    if request.method == 'POST':
          # _ = request.form['name']
        trainname = request.form['trainname']
        destination = request.form['destination']
        departuretime = request.form['departuretime']
        price = request.form['price']
        availablesits = request.form['availablesits']
        locationoftrain = request.form['locationoftrain']

        sql = 'INSERT INTO Train(trainname,destination,departuretime,price,availablesits,locationoftrain) VALUE (%s, %s,%s, %s,%s, %s)'
        val = (trainname, destination,departuretime,price, availablesits,locationoftrain)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM Train")
        train = mycursor.fetchall()
        return render_template('index.html', train = train)









@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_train(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Train WHERE ID={id}')
        train = mycursor.fetchone()
        return render_template('editdata.html', train = train)
    if request.method == 'POST':
        _trainname = request.form['trainname']
        _destination = request.form['destination']
        _departuretime = request.form['departuretime']
        _price = request.form['price']
        _availablesits = request.form['availablesits']
        _locationoftrain = request.form['locationoftrain']
        sql = f'UPDATE Train SET trainname = %s, destination = %s, departuretime=%s, price = %s, availablesits = %s, locationoftrain = %s WHERE ID = %s'
        values = (_trainname, _destination,_departuretime,_price, _availablesits,_locationoftrain,id)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.execute("SELECT * FROM Train")
        train = mycursor.fetchall()
        return render_template('index.html', train = train)





@app.route('/delete/<int:id>')
def delete_train(id):
    sql = f'DELETE FROM Train WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT * FROM Train")
    train = mycursor.fetchall()
    return render_template('index.html', train = train)







if __name__ == '__main__':
        app.run()




