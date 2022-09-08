from cw3_Dm_Vas.cw3_Dm_Vas.project.utils import *
from cw3_Dm_Vas.cw3_Dm_Vas.project.comments_utils import *

posts_keys = [key for key in get_all_posts()[0].keys()]
comments_keys = [key for key in get_all_comments()[0].keys()]


class TestUtils:

    def test_get_all(self):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = get_all_posts()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == set(posts_keys), "неверный список ключей"

    def test_get_by_id(self):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        post = get_post_by_pk(1)
        assert post["pk"] == 1, "возвращается неправильный кандидат"
        assert set(post.keys()) == set(posts_keys), "неверный список ключей"

    def test_get_by_username(self):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        post = get_posts_by_user("leo")
        assert post[0]["poster_name"] == "leo", "возвращается неправильный кандидат"
        assert set(post[0].keys()) == set(posts_keys), "неверный список ключей"

    def test_search(self):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        params = "ага"
        response = search_for_posts(params)
        assert set(response[0].keys()) == set(posts_keys), "неверный список ключей"
        assert len(response) != 0, "возвращается пустой список"

    def test_get_all_comments(self):
        """ Проверяем, верный ли список кандидатов возвращается """
        comments = get_all_comments()
        assert type(comments) == list, "возвращается не список"
        assert len(comments) > 0, "возвращается пустой список"
        assert set(comments[0].keys()) == set(comments_keys), "неверный список ключей"
