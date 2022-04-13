from flask_app import app
from flask import get_flashed_messages, jsonify, render_template, redirect, request, session, flash
from flask_app.models.vendor import Vendor

# CREATE ROUTE------------------------------------
@app.route('/create/vendor', methods=['POST'])
def create_vendor():
    print('Creating a vendor...')
    vendor_data = request.get_json()
    if not Vendor.validate_vendor(vendor_data):
        messages = get_flashed_messages(with_categories='true')
        errs = {}
        for category,description in messages:
            errs[category] = description
        return jsonify(message = 'There was an error', errs = errs)
    print(vendor_data)
    vendor = Vendor.save(vendor_data)
    session['id'] = vendor
    return jsonify(vendor = vendor)
    

# READ ROUTE--------------------------------------
@app.route('/api')
def hello_world():
    list = {'vendors': [
        {'id': '1', 'name': 'Johnny', 'description': 'Great with vintage boards','location': "Venice Beach", 'imageUrl': 'https://wellgroomedgentleman.com/media/images/Old_Man_with_Long_Beard_and_Hair.width-800.jpg'},
        {'id': '2', 'name': 'Chuck', 'description': 'Shaper from Santa Cruz','location': "Manhattan Beach",'imageUrl': 'https://www.smithoptics.com/dw/image/v2/BDPZ_PRD/on/demandware.static/-/Library-Sites-SmithSharedLibrary/default/dwd2f275ef/images/Athletes/YADIN_NICOL_500X500.jpg' },
        {'id': '3', 'name': 'Tyler', 'description': 'Quick turnaround time',  'location': "Santa Monica",'imageUrl': 'https://i.pinimg.com/originals/fb/c2/9e/fbc29e11f43bb0a19c5bbc2d141fb840.jpg'
        },
    ]}
    # {'photos': [{'first': 'https://guide-images.cdn.ifixit.com/igi/gneNiSuRUxKcnlbZ.full', 'second': 'https://preview.redd.it/fe72qcrm19c81.jpg?width=640&crop=smart&auto=webp&s=ca91746a21a3e501d519776da581e16643c90369', 'third': 'https://surf-station.com/wp-content/uploads/2013/10/ding-repair-8-1.jpg'}
    # ]}
    print('hellooooo!!!')
    return list
# UPDATE ROUTE------------------------------------
# DELETE ROUTE------------------------------------
