import json


def get_all_posts():
    """Returns all posts"""

    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def get_posts_by_user(user_name):
    """Get all posts of user by user_name, if such user exists"""

    data = get_all_posts()
    authors = [post['poster_name'] for post in data]
    posts = []
    try:
        if user_name in authors:
            for post in data:
                if user_name == post['poster_name']:
                    posts.append(post)
        else:
            raise ValueError
    except ValueError:
        return f'<h1>Пользователя {user_name} не найдено</h1>'
    else:
        return posts


def search_for_posts(query: str):
    """:returns all the posts by keyword"""

    posts_list: list = get_all_posts()
    posts = []
    for post in posts_list:
        if query.lower() in post['content'].lower().strip():
            posts.append(post)
    return posts


def get_post_by_pk(pk: str):
    """Возвращает пост по номеру"""

    post_list: list = get_all_posts()
    for post in post_list:
        if pk == post['pk']:
            return post
