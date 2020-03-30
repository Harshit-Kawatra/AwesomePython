from flask import Flask, Markup, render_template
import calc
app = Flask(__name__)
a=5
b=6

@app.route('/')
def calculator():
    add=calc.add(a,b)
    sub=calc.sub(a,b)
    mul=calc.mul(a,b)
    div=calc.div(a,b)
    return render_template('calc.html', add=add, sub=sub,mul=mul,div=div)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)