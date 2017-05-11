import sys
from scrape_album import *
from flask import Flask, make_response, render_template, flash, redirect
from forms import url_form

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = url_form()
    if form.validate_on_submit():
        scrape_index(form.url_field.data)
        return redirect('/')
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()
