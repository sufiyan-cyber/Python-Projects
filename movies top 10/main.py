from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,FloatField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("apikey")
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = api_key


URL=f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query="


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class editform(FlaskForm):
    newrating = FloatField(u'Rating')
    newreview = StringField(u'Review', validators=[DataRequired()])
    submit=SubmitField("Done")
# CREATE DB
class addform(FlaskForm):
    movietitle=StringField("Movie title",validators=[DataRequired()])
    submit=SubmitField("Add")

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMzU3MTRlYTlkODliYTZlNmU5NTdhNTUxM2RlNmNmOSIsIm5iZiI6MTc3MDgwMTI2NC4xMTEsInN1YiI6IjY5OGM0ODcwNzA3NzA2MjFjZWE2MTUyMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VqjmXO-X6NaZa0vkoMxT8aXziOHNThaf3slXF7sL80k"
}


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] =mapped_column(String(250),nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] =mapped_column(Integer)
    review:Mapped[str] =mapped_column(String(250))
    img_url:Mapped[str] =mapped_column(String(500),nullable=False)

# CREATE TABLE

'''with app.app_context():
    db.create_all()

    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )

    db.session.add(second_movie)
    db.session.commit()

'''
class DeleteForm(FlaskForm):
    pass

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    movies = result.scalars().all()

    # assign ranking dynamically
    for index, movie in enumerate(movies):
        movie.ranking = index + 1

    db.session.commit()
    form = DeleteForm()

    return render_template("index.html", movies=movies,form=form)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def editing(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    form = editform()

    if form.validate_on_submit():
        movie.rating = form.newrating.data
        movie.review = form.newreview.data

        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:movie_id>", methods=["GET", "POST"])  # Add GET if you want to allow simple link deletes
def deleting(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    if request.method == "POST":
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('home'))

    # Optional: If someone accidentally navigates to /delete/1 via GET
    return redirect(url_for('home'))


@app.route("/add",methods=["GET","POST"])
def adding():
    form=addform()
    if form.validate_on_submit():
        title=form.movietitle.data

        response = requests.get(f"{URL}{title}", headers=headers)


        jsonform = response.json()

        movies = {}

        for movie in jsonform["results"]:
            movie_id = movie["id"]
            title = movie["title"]
            release = movie["release_date"]

            year = release[:4] if release else "N/A"

            movies[movie_id] = {
                "title": title,
                "year": year
            }


        return render_template("select.html",movies=movies)
    return render_template("add.html",form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")

    if not movie_api_id:
        return redirect(url_for("home"))

    # get movie details from TMDB
    movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
    response = requests.get(
        movie_api_url,
        params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"}
    )

    data = response.json()

    # prevent duplicate insertion
    existing = db.session.execute(
        db.select(Movie).where(Movie.title == data["title"])
    ).scalar()

    if existing:
        return redirect(url_for("home"))

    # release date safety
    release_date = data.get("release_date")
    year = int(release_date.split("-")[0]) if release_date else 0

    # poster safety
    poster_path = data.get("poster_path")
    img_url = f"{MOVIE_DB_IMAGE_URL}{poster_path}" if poster_path else ""

    # overview safety
    description = data.get("overview") or "No description available."

    # IMPORTANT: rating & ranking cannot be NULL in your DB
    new_movie = Movie(
        title=data["title"],
        year=year,
        description=description,
        img_url=img_url,
        rating=0.0,
        ranking=0,
        review=""
    )

    db.session.add(new_movie)
    db.session.commit()

    # send user to rating page
    return redirect(url_for("editing", movie_id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
