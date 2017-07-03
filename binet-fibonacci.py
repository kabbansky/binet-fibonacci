#!/usr/bin/env python
import flask
from flask import Flask, request, Response
import sys, math, decimal
from math import sqrt
from decimal import Decimal

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api_help():
    return app.send_static_file('help.html')

@app.route('/api/<int:n>', methods=['GET'])
def main(n):
    
    #go for some higher precision with Decimal
    gr = Decimal((1 + sqrt(5)) / 2 )
    div = Decimal(2 * gr - 1 )

    #the Binet formula
    ln = round(Decimal(( pow(gr,n) - pow(-gr,-n) ) / div ))

    #actually this script works in range -1476..1476
    #here could be another if clause

    if str(ln) == "inf":
        return "Sorry, the number is too big"
        sys.exit(0)
    else:
        return str("%d" % ln)

if __name__ == "__main__":
    app.run()
