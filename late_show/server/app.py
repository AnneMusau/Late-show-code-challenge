from flask import Flask, jsonify, request, make_response
from models import db, Episode, Guest, Appearance
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

class Home(Resource):
    def get(self):
        return make_response(jsonify({"message": "Welcome to the Newsletter RESTful API"}), 200)

api.add_resource(Home, '/')

class EpisodesResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        response_dict_list = [episode.to_dict() for episode in episodes]
        return make_response(jsonify(response_dict_list), 200)

api.add_resource(EpisodesResource, '/episodes')

class GuestsResource(Resource):
    def get(self):
        guests = Guest.query.all()
        response_dict_list = [guest.to_dict() for guest in guests]
        return make_response(jsonify(response_dict_list), 200)

api.add_resource(GuestsResource, '/guests')

class AppearanceResource(Resource):
    def post(self):
        new_appearance = Appearance(
            rating=request.json.get('rating'),
            episode_id=request.json.get('episode_id'),
            guest_id=request.json.get('guest_id')
        )
        db.session.add(new_appearance)
        db.session.commit()
        return make_response(jsonify(new_appearance.to_dict()), 201)

    def patch(self, id):
        appearance = Appearance.query.get(id)
        if not appearance:
            return make_response({"message": "Appearance not found"}, 404)

        # Update only the fields that are present in the request
        if 'rating' in request.json:
            appearance.rating = request.json['rating']
        if 'episode_id' in request.json:
            appearance.episode_id = request.json['episode_id']
        if 'guest_id' in request.json:
            appearance.guest_id = request.json['guest_id']

        db.session.commit()
        return make_response(jsonify(appearance.to_dict()), 200)

    def delete(self, id):
        appearance = Appearance.query.get(id)
        if not appearance:
            return make_response({"message": "Appearance not found"}, 404)

        db.session.delete(appearance)
        db.session.commit()
        return make_response({"message": "Appearance successfully deleted"}, 200)

api.add_resource(AppearanceResource, '/appearances')

class AppearanceByID(Resource):
    def get(self, id):
        appearance = Appearance.query.get(id)
        if not appearance:
            return make_response({"message": "Appearance not found"}, 404)
        return make_response(jsonify(appearance.to_dict()), 200)

api.add_resource(AppearanceByID, '/appearances/<int:id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  

    app.run(debug=True, port=5555)
