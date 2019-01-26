from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\nOperation?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    x = Fraction(value1)
    y= Fraction(value2)
    result=value1+value2
    temp = str(result).split('/')
    if len(temp) == 2:
        d = int(temp[0])/int(temp[1])
        de = str(d).split('.')
        if de[1] == '0':
            return '%s \n'% de[0]
        else:
            return '%s \n' % d
    else:
        s=str(result).split('.')
        return '%s \n'% s[0]


if __name__ == "__main__":
    app.run()
