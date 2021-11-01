import datetime
from io import StringIO
from flask import Flask, request, Response
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
import csv
import sqlite3 as sq
import pandas as pd

app = Flask(__name__)
api = Api(app)

# defining database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///covid.db'
db = SQLAlchemy(app)


class Death(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(50))
    state = db.Column(db.String(100))
    combined = db.Column(db.String(200))
    cases = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"Death('{self.country}','{self.state}', '{self.combined}', " \
               f"'{self.cases}', '{self.date}')"


class Confirmed(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(50))
    state = db.Column(db.String(100))
    combined = db.Column(db.String(200))
    cases = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"Confirmed('{self.country}','{self.state}', " \
               f"'{self.combined}', '{self.cases}', '{self.date}')"


class Active(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(50))
    state = db.Column(db.String(100))
    combined = db.Column(db.String(200))
    cases = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"Active('{self.country}','{self.state}', '{self.combined}', " \
               f"'{self.cases}', '{self.date}')"


class Recovered(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(50))
    state = db.Column(db.String(100))
    combined = db.Column(db.String(200))
    cases = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f"Recovered('{self.country}','{self.state}', '{self.combined}', " \
               f"'{self.cases}', '{self.date}')"


@app.route('/time_series/<data_type>', methods=['POST', 'PUT'])
def upload_time_series(data_type):
    # file = request.files['file']
    # TODO: the below must be replaced by getting from request
    #      <data_type> can be 'death', 'confirmed', 'active', 'recovered'
    file = open("test/time_series_test.csv")

    # below are database ops
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    c1, c2, c3, date_start, success = locate_columns_time_series(header)
    if not success:
        return Response("Invalid csv form", status=400)
    if data_type.lower() == 'death':
        row = next(reader)
        while row is not None:
            try:
                for i in range(date_start, len(row)):
                    if c3 == -1:
                        comb = ""
                    else:
                        comb = row[c3]
                    date = datetime.datetime.strptime(str(datetime.datetime.strptime(header[i], '%m/%d/%y').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
                    existing = Death.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                    if existing is None:
                        new_row = Death(country=row[c1], state=row[c2],
                                        combined=comb, cases=row[i],
                                        date=date)
                        if row[i] != '':
                            db.session.add(new_row)
                    else:
                        existing.cases = row[i]
                    db.session.commit()
            except:
                return Response("Cannot add to database", status=500)
            try:
                row = next(reader)
            except StopIteration:
                row = None
    elif data_type.lower() == 'confirmed':
        row = next(reader)
        while row is not None:
            print(row)
            try:
                for i in range(date_start, len(row)):
                    if c3 == -1:
                        comb = ""
                    else:
                        comb = row[c3]
                    date = datetime.datetime.strptime(str(datetime.datetime.strptime(header[i], '%m/%d/%y').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
                    existing = Confirmed.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                    if existing is None:
                        new_row = Confirmed(country=row[c1], state=row[c2],
                                            combined=comb, cases=row[i],
                                            date=date)
                        if row[i] != '':
                            db.session.add(new_row)
                    else:
                        existing.cases = row[i]
                    db.session.commit()
            except:
                return Response("Cannot add to database", status=500)
            try:
                row = next(reader)
            except StopIteration:
                row = None
    elif data_type.lower() == 'active':
        row = next(reader)
        while row is not None:
            print(row)
            try:
                for i in range(date_start, len(row)):
                    if c3 == -1:
                        comb = ""
                    else:
                        comb = row[c3]
                    date = datetime.datetime.strptime(str(datetime.datetime.strptime(header[i], '%m/%d/%y').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
                    existing = Active.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                    if existing is None:
                        new_row = Active(country=row[c1], state=row[c2],
                                         combined=comb, cases=row[i],
                                         date=date)
                        if row[i] != '':
                            db.session.add(new_row)
                    else:
                        existing.cases = row[i]
                    db.session.commit()
            except:
                return Response("Cannot add to database", status=500)
            try:
                row = next(reader)
            except StopIteration:
                row = None
    elif data_type.lower() == 'recovered':
        row = next(reader)
        while row is not None:
            print(row)
            try:
                for i in range(date_start, len(row)):
                    if c3 == -1:
                        comb = ""
                    else:
                        comb = row[c3]
                    date = datetime.datetime.strptime(str(datetime.datetime.strptime(header[i], '%m/%d/%y').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
                    existing = Recovered.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                    if existing is None:
                        new_row = Recovered(country=row[c1], state=row[c2],
                                            combined=comb, cases=row[i],
                                            date=date)
                        if row[i] != '':
                            db.session.add(new_row)
                    else:
                        existing.cases = row[i]
                    db.session.commit()
            except:
                return Response("Cannot add to database", status=500)
            try:
                row = next(reader)
            except StopIteration:
                row = None
    else:
        return Response("Invalid request form, need .../time_series/<data_type>"
                        , status=400)

    return Response("Success", status=201)


@app.route('/daily_reports/', methods=['POST', 'PUT'])
def upload_daily_reports():
    # file = request.files['file']

    # TODO:the below must be replaced by getting from request
    file = open("test/daily_report_test.csv")

    # below are database ops
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    c1, c2, c3, c_date, c_death, c_confirmed, c_active, c_recovered, success = locate_columns_daily_report(header)
    if not success:
        return Response("Invalid csv form", status=400)
    row = next(reader)
    while row is not None:
        if c3 == -1:
            comb = ""
        else:
            comb = row[c3]

        if c_death != -1:
            date = datetime.datetime.strptime(str(datetime.datetime.strptime(row[c_date], '%Y-%m-%d %H:%M:%S').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
            try:
                existing = Death.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                if existing is None:
                    new_row = Death(country=row[c1], state=row[c2],
                                    combined=comb, cases=row[c_death],
                                    date=date)
                    if row[c_death] != '':
                        db.session.add(new_row)
                else:
                    existing.cases = row[c_death]
                db.session.commit()
            except:
                return Response("Cannot add to database", status=500)

        if c_confirmed != -1:
            date = datetime.datetime.strptime(str(datetime.datetime.strptime(row[c_date], '%Y-%m-%d %H:%M:%S').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
            try:
                existing = Confirmed.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                if existing is None:
                    new_row = Confirmed(country=row[c1], state=row[c2],
                                        combined=comb, cases=row[c_confirmed],
                                        date=date)
                    if row[c_confirmed] != '':
                        db.session.add(new_row)
                else:
                    existing.cases = row[c_confirmed]
                db.session.commit()
            except:
                return Response("Cannot add to database", status=500)

        if c_active != -1:
            date = datetime.datetime.strptime(str(datetime.datetime.strptime(row[c_date], '%Y-%m-%d %H:%M:%S').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
            try:
                existing = Active.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                if existing is None:
                    new_row = Active(country=row[c1], state=row[c2],
                                        combined=comb, cases=row[c_active],
                                        date=date)
                    if row[c_active] != '':
                        db.session.add(new_row)
                else:
                    existing.cases = row[c_active]
                db.session.commit()
            except:
                return Response("Cannot add to database", status=500)

        if c_recovered != -1:
            date = datetime.datetime.strptime(str(datetime.datetime.strptime(row[c_date], '%Y-%m-%d %H:%M:%S').date()) + ' 00:00:00.0', "%Y-%m-%d %H:%M:%S.%f")
            try:
                existing = Recovered.query.filter_by(country=row[c1], state=row[c2], combined=comb, date=date).first()
                if existing is None:
                    new_row = Recovered(country=row[c1], state=row[c2],
                                        combined=comb, cases=row[c_recovered],
                                        date=date)
                    if row[c_recovered] != '':
                        db.session.add(new_row)
                else:
                    existing.cases = row[c_recovered]
                db.session.commit()
            except:
                return Response("Cannot add to database", status=500)
        try:
            row = next(reader)
        except StopIteration:
            row = None
    return Response("Success", status=201)


@app.route('/cases', methods=['GET'])
def get_info():

    # TODO: get the following info from request, hardcoded for now.
    #  format List[<tup>,...,<tup>], each tuple has
    #  (country, state/province, combined_key, start date, end date, type of data)
    #  empty string for info that is not given, start date=end date if only
    #  querying for one single day.
    query = [('Canada', 'British Columbia', '', '2020-01-22', '2020-01-26', 'death'),
             ('US', 'South Carolina', 'Abbeville, South Carolina, US', '2020-06-06', '2020-06-06', 'active'),
             ('Bahamas', '', '', '2020-01-23', '2020-07-01', 'death')]
    # TODO: get output format from request, csv or json
    output_format = 'json'

    # Below are database ops
    con = sq.connect('covid.db')
    result = []
    for q in query:
        sql_query = "select country as 'country/region', state as 'state/province', combined as 'combined_key', date(date) as date, cases, '%s' as 'type' " \
                    "from %s where country='%s' and state='%s' and combined='%s' and date >= '%s' and " \
                    "date < DATE('%s', '+1 day');" % (q[5], q[5], q[0], q[1], q[2], q[3], q[4])
        result.append(pd.read_sql(sql_query, con))

    final = pd.concat(result, ignore_index=True)
    print(final)
    output = StringIO()

    if output_format == 'csv':
        final.to_csv(output)
        return Response(output.getvalue(), mimetype="text/csv", status=200)
    else:  # default json
        print("hey")
        output = final.to_json(orient='records')
        return Response(output, status=200)


def locate_columns_time_series(lst):
    success = True
    c1 = -1
    c2 = -1
    c3 = -1
    date_start = -1
    for i in range(len(lst)):
        if 'country' in lst[i].lower() or 'region' in lst[i].lower():
            c1 = i
        elif 'state' in lst[i].lower() or 'province' in lst[i].lower():
            c2 = i
        elif 'combined' in lst[i].lower():
            c3 = i
        elif validate_date(lst[i]) and date_start == -1:
            date_start = i
    if c1 == -1 or c2 == -1 or date_start == -1:
        success = False
    return c1, c2, c3, date_start, success


def locate_columns_daily_report(lst):
    success = True
    c1 = -1
    c2 = -1
    c3 = -1
    c_date = -1
    c_death = -1
    c_confirmed = -1
    c_active = -1
    c_recovered = -1

    for i in range(len(lst)):
        if 'country' in lst[i].lower() or 'region' in lst[i].lower():
            c1 = i
        elif 'state' in lst[i].lower() or 'province' in lst[i].lower():
            c2 = i
        elif 'combined' in lst[i].lower():
            c3 = i
        elif 'last' in lst[i].lower() or 'update' in lst[i].lower():
            c_date = i
        elif 'death' in lst[i].lower():
            c_death = i
        elif 'confirm' in lst[i].lower():
            c_confirmed = i
        elif 'active' in lst[i].lower():
            c_active = i
        elif 'recover' in lst[i].lower():
            c_recovered = i
    if c1 == -1 or c2 == -1 or c_date == -1:
        success = False
    return c1, c2, c3, c_date, c_death, c_confirmed, c_active, \
        c_recovered, success


def validate_date(date):
    b = 2
    try:
        datetime.datetime.strptime(date, '%m/%d/%y')
    except ValueError:
        b -= 1
    try:
        datetime.datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        b -= 1
    return bool(b)


if __name__ == "__main__":
    app.run(debug=True)  # TODO: change to false for production

    # upload_time_series("death")
    # upload_daily_reports()
    # get_info()
