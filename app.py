import sys
from scrape_album import *
from flask import Flask, make_response, render_template, flash, redirect
from models.forms import search_form, search_again

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    title = 'Bandcamp Visualizer'
    form = search_form()
    if form.validate_on_submit():
        scrape_search(form.search_field.data)
        return redirect('/stats')
    return render_template('index.html', title=title, form=form)

@app.route('/stats', methods=['GET', 'POST'])
def stats():
    title = 'Stats Display'
    form = search_again()
    if form.validate_on_submit():
        scrape_search(form.search_field.data)
        return redirect('/stats')
    return render_template('stats.html', title=title, form=form)


if __name__ == "__main__":
    app.run()
