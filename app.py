from flask import Flask, render_template, request
from algo.algo_handler import handle

app = Flask(__name__)

@app.route('/')
def index():
    (clear_text, cryted_text, frequency_list, is_success, action) = handle(request.args)
    error_message = ""
    if not is_success:
        error_message = clear_text
        return render_template("index.html", error_message=error_message)
    else:
        return render_template("index.html", clear_text=clear_text, crypted_text=cryted_text, frequency_list=frequency_list)

@app.route('/api')
def raw_format():
    (clear_text, cryted_text, frequency_list, is_success, action) = handle(request.args)
    if not is_success:
        return clear_text
    else:
        return "Texte en clair : {0}<br> Texte crypté : {1} <br> Analyse frequentielle : {2}".format(clear_text, cryted_text, frequency_list)
    #return handle(request.args)
    #return render_template("index.html", algo="testsfgdfgdsc")
