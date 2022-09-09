from flask import Flask

from coursework3_Dm_Vas.project.posts_views import posts_blueprint
from coursework3_Dm_Vas.project.bookmarks_views import boookmarks_blueprint

app = Flask(__name__)

app.json.ensure_ascii

app.register_blueprint(posts_blueprint)
app.register_blueprint(boookmarks_blueprint)


if __name__ == "__main__":
    app.run()