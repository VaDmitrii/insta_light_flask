# Social network on Flask with basic pages

### Stack used: HTML, flask, Jinja, Python

### The API reads data from .json files, render different templates on several endpoints and wright request logs to api.log file.

* '/' - feed endpoint. Script reads posts.json file and renders the main page (index.html) with all the posts and comments
* '/posts/post_id/' - post endpoint. Reads posts.json file and renders post.html template with post and its comments by post_id data
* '/users/username/' - user feed page. Reads posts.json file and renders user-feed.html template with all posts and its comments by username
* '/search/' - posts by keyword. Reads posts.json file and renders search.html template with all posts and its comments that contain keyword from request.args
* '/bookmarks/' - user's bookmarks page. Reads bookmarks.json file and renders bookmarks.html template with all posts saved to bookmarks
* '/bookmarks/add/post_id' - adding post to bookmarks. Bookmark icon on each post allows to save the post to bookmarks.json file
* '/bookmarks/remove/post_id' - deleting post from bookmarks. Delete post from bookmarks.json file and return user to index.html page

## How to run API
- Create virtual environment

- Install requirement form requirements.txt file
```
pip install -r requirements.txt

```
- Run API
```
flask --app run run
```
