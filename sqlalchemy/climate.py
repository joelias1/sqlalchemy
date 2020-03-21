from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return (
        f'Routes Use:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end>'
    
    )

@app.route('/api/v1.0/precipitation')
def precipitation() :
        last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        prev_year = maxDate - dt.timedelta(days=365) 
# Performing a query
           
        temp_df = (session.query(Measurement.date, Measurement.prcp)
                  .filter(Measurement.date <= maxDate)
                  .filter(Measurement.date >= year_ago)
                  .order_by(Measurement.date).all())
    
        precip = {date: prcp for date, prcp in temp_df}
    
        return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():

    stations_all = session.query(Station.station).all()

    return jsonify(stations_all)

@app.route('/api/v1.0/tobs') 
def tobs():  
    maxDate = dt.date(2017, 8 ,23)
    prev_year = maxDate - dt.timedelta(days=365)

    temp_df = (session.query(Measurement.tobs)
                .filter(Measurement.station == 'USC00519281')
                .filter(Measurement.date <= maxDate)
                .filter(Measurement.date >= year_ago)
                .order_by(Measurement.tobs).all())
    
    return jsonify(lastyear)

@app.route('/api/v1.0/<start>') 
def start(start=None):

    

    start_queries = (session.query(Measurement.tobs).filter(Measurement.date.between(start, '2017-08-23')).all())
    
    start_df = pd.DataFrame(tobs_only)

    tavg = tobs_df["tobs"].mean()
    tmax = tobs_df["tobs"].max()
    tmin = tobs_df["tobs"].min()
    
    return jsonify(tavg, tmax, tmin)

@app.route('/api/v1.0/<start>/<end>') 
def startend(start=None, end=None):

   
    tobs_only = (session.query(Measurement.tobs).filter(Measurement.date.between(start, end)).all())
    
    tobs_df = pd.DataFrame(tobs_only)

    tavg = tobs_df["tobs"].mean()
    tmax = tobs_df["tobs"].max()
    tmin = tobs_df["tobs"].min()
    
    return jsonify(tavg, tmax, tmin)

if __name__ == '__main__':
    app.run(debug=True)

