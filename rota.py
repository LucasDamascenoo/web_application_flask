from flask import Flask, render_template
app = Flask(__name__)

@app.route('/inicio/')
def teste():
   return render_template('teste.html')

app.run()
