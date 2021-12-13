from flask import Blueprint
from flask import make_response, jsonify, request
from werkzeug.exceptions import abort
import datetime
import calendar
import sys

bp = Blueprint("availability", __name__)

days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ]

@bp.route("/")
def index():
    args = request.args

    year = args["year"]
    month = args["month"]
    day = args["day"]

    date = datetime.datetime(int(year), int(month), int(day), 12, 00, 00)

    print(date, file=sys.stderr)

    dayOfTheWeek = calendar.day_name[date.weekday()]

    workingDay = dayOfTheWeek in days

    if workingDay == False:
        return { "workingDay": workingDay }, 400
    return { "workingDay": workingDay }, 200
