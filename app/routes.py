from flask import render_template, flash, redirect
from app import app, logged_in
from app.forms import SearchForm, LoginForm
import scrape

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home', logged_in=logged_in)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in, browser
    # logged_in = 1 # just for testing
    form = LoginForm()
    if form.validate_on_submit():
        if logged_in:
            flash('You are already logged in to Netflix! and logged_in has value '+str(logged_in))
            return redirect('search')            
        else:
            logged_in=scrape.netflix_login(form)   
            if logged_in:
                flash('You are are now logged in to Netflix! and logged_in has value '+str(logged_in))
                return redirect('search')
            else:
                flash('Something went wrong, try to login again. logged_in has value '+str(logged_in))   
                return redirect('login') 
    flash('You are NOT logged in and logged_in has value '+str(logged_in))
    return render_template('login.html', title='Login', form=form, logged_in=logged_in)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    None

@app.route('/search', methods=['GET', 'POST'])
def search():
    global browser, logged_in
    form = SearchForm()
    if form.validate_on_submit():
        searches=form.filmname.data.split(";")
        results={}
        for search in searches:
            links, imgs = scrape.film_search(search)
            #flash('Here are the first 3 hits from NetFlix PT for your search "' + form.filmname.data + '":')
            #links, imgs = ['Hubba', 'Hopp', 'HIPP!!!'], ['https://occ-0-2268-360.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABRoyYWcBJnZbLPTgIYMOvJJ8LOLuPhMvV5nghrIESgPlgSyA9FWC4PaSUcxWVsNG-AYq5B6AYT8n-NlBBhxQaQJ4LCw.webp?r=285','https://occ-0-2268-360.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABRoyYWcBJnZbLPTgIYMOvJJ8LOLuPhMvV5nghrIESgPlgSyA9FWC4PaSUcxWVsNG-AYq5B6AYT8n-NlBBhxQaQJ4LCw.webp?r=285','https://occ-0-2268-360.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABRoyYWcBJnZbLPTgIYMOvJJ8LOLuPhMvV5nghrIESgPlgSyA9FWC4PaSUcxWVsNG-AYq5B6AYT8n-NlBBhxQaQJ4LCw.webp?r=285']
            results[search]=[links, imgs]
        return render_template('results.html', title='Search Result', results=results, logged_in=logged_in)
    return render_template('search.html', title='Home', form=form, logged_in=logged_in)

