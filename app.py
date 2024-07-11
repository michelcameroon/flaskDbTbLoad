from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

import fieldNamesInTable

app = Flask(__name__)

app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solarCalc6.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#migrate = Migrate(app, db)
app.app_context().push()

class Load(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nameBrand = db.Column(db.String(100), nullable=False)
    powerWatts = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    day_duration = db.Column(db.Integer, nullable=False)
    night_duration = db.Column(db.Integer, nullable=False)

   
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load')
def list_loads():
    loads = Load.query.all()
    print (loads)
    names = fieldNamesInTable.names('instance/solarCalc6.db', 'load')
    print (names)

    return render_template('list.html', loads=loads, names=names)
        



@app.route('/load/new', methods=['GET', 'POST'])
def new_load():
    if request.method == 'POST':
        
        names = fieldNamesInTable.names('instance/solarCalc6.db', 'load')
        print (names)
        '''
        values = ''
        value = ''
        for name in names:
            #if name != 'id':
            value = request.form[name]
            if values  == '':
                values = name + '=' + value
            else:
                values = values + ', ' +  name +  '=' + value
        '''

        '''
        nameBrand = request.form['nameBrand']
        powerWatts = request.form['powerWatts']
        number = request.form['number']
        day_duration = request.form['day_duration']
        night_duration = request.form['night_duration']
        
        print ('nameBrand=')        
        print (nameBrand)        
        '''
        #new_load = Load(nameBrand=nameBrand, powerWatts=powerWatts, number=number, day_duration=day_duration, night_duration=night_duration)
        #new_load = Load(nameBrand=nameBrand, powerWatts=1, number=2, day_duration=3, night_duration=4) 	# working


        '''
        
        print (values)
        new_load = Load(values)
        print ('new_load=')
        print (new_load)
         
        db.session.add(new_load)
        print (new_load)
        '''
        #data = {field_name: request.form[field_name] for field_name in field_names}
        data = {name: request.form[name] for name in names}
        print ('data=')
        print (data)
        new_record = MyModel(**data)

        db.session.add(new_record)

        #db.session.commit()






        db.session.commit()
        return redirect(url_for('list_loads'))
    return render_template('new.html')

@app.route('/load/update/<int:id>', methods=['GET', 'POST'])
def update_load(id):
    load = Load.query.get_or_404(id)
    names = fieldNamesInTable.names('instance/solarCalc6.db', 'load')

    if request.method == 'POST':
        
        print (names)
  
        for name in names:
            if name != 'id':
               name1 = "'" + name + "'"
               print ('name1=')
               print (name1)
               load.name = request.form[name1]
 


        '''

        load.nameBrand = request.form['nameBrand']
        load.powerWatts = request.form['powerWatts']
        load.number = request.form['number']
        load.day_duration = request.form['day_duration']
        load.night_duration = request.form['night_duration']
        '''

            
        db.session.commit()
        return redirect(url_for('list_loads'))
    #return render_template('update.html', load=load)
    return render_template('update.html', load=load, names=names)

@app.route('/load/delete/<int:id>', methods=['GET', 'POST'])
def delete_load(id):
    load = Load.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(load)
        db.session.commit()
        return redirect(url_for('list_loads'))
    return render_template('delete.html', load=load)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
