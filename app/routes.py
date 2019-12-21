from flask import render_template, flash, redirect
from app import app
from app.forms import SearchForm
import scrape

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global browser
    form = SearchForm()
    if form.validate_on_submit():
        browser = scrape.netflix_login()
        browser, links, imgs = scrape.film_search(browser, form.filmname.data)
        flash('Here are the first 3 hits from NetFlix PT for your search "' + form.filmname.data + '":')
        #browser, links, imgs = 1, ['Hubba', 'Hopp', 'HIPP!!!'], ['https://occ-0-2268-360.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABRoyYWcBJnZbLPTgIYMOvJJ8LOLuPhMvV5nghrIESgPlgSyA9FWC4PaSUcxWVsNG-AYq5B6AYT8n-NlBBhxQaQJ4LCw.webp?r=285','https://occ-0-2268-360.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABRoyYWcBJnZbLPTgIYMOvJJ8LOLuPhMvV5nghrIESgPlgSyA9FWC4PaSUcxWVsNG-AYq5B6AYT8n-NlBBhxQaQJ4LCw.webp?r=285','https://occ-0-2268-360.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABRoyYWcBJnZbLPTgIYMOvJJ8LOLuPhMvV5nghrIESgPlgSyA9FWC4PaSUcxWVsNG-AYq5B6AYT8n-NlBBhxQaQJ4LCw.webp?r=285']
        #film_search('filmname')
        #return redirect('index')
        return render_template('results.html', title='Search Result', links=links, imgs=imgs)
    return render_template('index.html', title='Home', form=form)


