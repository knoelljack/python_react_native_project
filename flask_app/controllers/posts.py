from crypt import methods
from email import message
import json
from operator import methodcaller
from pyexpat.errors import messages
from flask_app import app
from flask import get_flashed_messages,request,session,jsonify
from flask_app.models.post import Post

#CREATE A POST
@app.route('/create/post', methods=['POST'])
def create_post():
    print('Creating a post...')
    post_data = request.get_json()
    if not Post.validate_post(post_data):
        messages = get_flashed_messages(with_categories='true')
        errs = {}
        for category,description in messages:
            errs[category] = description
        return jsonify(message = 'There was an error', errs = errs)
    creator_id = session['id']
    post_data = {
        **request.get_json(),
        'user_id' : creator_id
    }
    post = Post.save(post_data)
    return jsonify(post=post)
