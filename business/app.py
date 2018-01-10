from flask_api import FlaskAPI
from instance.config import app_config
from datamodel.models import db, Farm
from flask import jsonify, abort, request


def create_app():
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/')
    def hello():
        return "Hello Smart Farm"

    @app.route('/farmlist/<string:name>', methods=['GET', 'PUT', 'DELETE'])
    def getfarm(name, **kwargs):
        farm = Farm.query.filter_by(name=name).first()
        if not farm:
            abort(404)
        if request.method == 'DELETE':
            farm.delete()
            response = jsonify({'message': 'Farm {0} deleted succesfully'.format(farm.name)})

        else:
            if request.method == 'PUT':
                address = str(request.data.get('address', ''))
                farm.address = address
                farm.save()
                response = jsonify({
                    'address': farm.address
                })

            else:
                if request.method == 'GET':
                    response = jsonify({

                        'name': farm.name,
                        'address': farm.address

                    })
        response.status_code = 200
        return response

    @app.route('/farmlist/', methods=['GET', 'POST'])
    def farmlist():
        if request.method == 'POST':
            name = str(request.data.get('name', ''))
            address = str(request.data.get('address', ''))
            farm = Farm(name=name, address=address)
            farm.save()
            response = jsonify(
                {

                    'name': farm.name,
                    'address': farm.address

                }
            )
            response.status_code = 201

        else:
            if request.method == 'GET':
                farmlist = Farm.get_all()
                results = []
                for farm in farmlist:
                    obj = {

                        'name': farm.name,
                        'address': farm.address

                    }
                    results.append(obj)
                response = jsonify(results)
                response.status_code = 200
        return response

    return app
