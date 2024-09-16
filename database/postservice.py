from database.models import UserPost, Comment, Hashtags
from database import get_db


# Функуция для создания поста
def add_user_post_db(user_id, main_text, hashtag=None):
    with next(get_db()) as db:
        new_post = UserPost(user_id=user_id, main_text=main_text,
                            hashtag=hashtag)
        db.add(new_post)
        db.commit()
        return new_post.id


# Функция для получения всех постов
def get_all_posts_db():
    with next(get_db()) as db:
        return db.query(UserPost).all()


# Функия для получения определенного поста по его id
def get_exact_post_db(post_id):
    with next(get_db()) as db:
        exact_post = db.query(UserPost).filter_by(id=post_id).first()
        if exact_post:
            return exact_post
        return False


# Функция для изменения текста поста
def change_post_db(post_id, new_text):
    with next(get_db()) as db:
        post_to_edit = db.query(UserPost).filter_by(id=post_id).first()
        if post_to_edit:
            post_to_edit.main_text = new_text
            db.commit()
            return True
        return False


# Функция для удаления поста
def delete_post_db(post_id):
    with next(get_db()) as db:
        post_to_delete = db.query(UserPost).filter_by(id=post_id).first()
        if post_to_delete:
            db.delete(post_to_delete)
            db.commit()
            return True
        return False


# Функция для добавления комментария
def add_comment_to_post_db(user_id, post_id, text):
    with next(get_db()) as db:
        new_comment = Comment(comment=text, user_id=user_id,
                              post_id=post_id)
        db.add(new_comment)
        db.commit()
        return new_comment.id


# Функция для получения комментария у поста
def get_comment_by_post_id_db(post_id):
    with next(get_db()) as db:
        exact_post = db.query(UserPost).filter_by(
            id=post_id).first()
        if exact_post:
            get_comment = db.query(Comment).filter_by(
                post_id=post_id).all()
            return get_comment
        return False


# Функуция для изменения текста у коммента
def change_comment_text_db(comment_id, new_text):
    with next(get_db()) as db:
        comment = db.query(Comment).filter_by(id=comment_id).first()
        if comment:
            comment.comment = new_text
            db.commit()
            return True
        return False


# Функция для удаления коммента по id
def delete_comment_db(comment_id):
    with next(get_db()) as db:
        delete_comment = db.query(Comment).filter_by(id=comment_id).first()
        if delete_comment:
            db.delete(delete_comment)
            db.commit()
            return True
        return False


# Функция для добавления хэштегов
def add_hashtag_db(hashtag_name):
    with next(get_db()) as db:
        new_hashtag = Hashtags(hashtag_name=hashtag_name)
        db.add(new_hashtag)
        db.commit()
        return new_hashtag.id


# Функция для получения топ постов по хэштегу
def get_post_by_hashtag_db(size, hashtag_name):
    with next(get_db()) as db:
        exact_hashtag = db.query(Hashtags).filter_by(hashtag_name=hashtag_name).first()
        if exact_hashtag:
            exact_posts = db.query(UserPost).filter_by(
                hashtag=hashtag_name).limit(size).all()
            return exact_posts
        return False


# Функция для получения хэштега по названию хэштега
def get_hashtag_db(hashtag_name):
    with next(get_db()) as db:
        exact_hashtag = db.query(Hashtags).filter_by(
            hashtag_name=hashtag_name).first()
        if exact_hashtag:
            return exact_hashtag
        return False
