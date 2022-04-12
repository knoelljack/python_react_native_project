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
    post = Post.create(post_data)
    return jsonify(post=post)

#DELETE A POST
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_post(id):
    post_data = {
        'id' : id
    }
    delete = Post.delete_post(post_data)
    print('Deleted post: ', delete)
    return jsonify(id=id)

#EDIT A POST
@app.route('/edit/post/<int:id>', methods=['PUT'])
def update_post(id):
    post_data = {
        **request.get_json(),
        'id' : id
    }
    print("Updating post with: ", post_data)
    post = Post.edit_post(post_data)
    print(post)
    return jsonify(id=id)

#SHOW ONE POST
@app.route('/posts/<int:id>', methods=['GET'])
def show_post(id):
    post = Post.get_post_by_id(id=id)
    print("Fetching post: ", post)
    return jsonify(post=post)