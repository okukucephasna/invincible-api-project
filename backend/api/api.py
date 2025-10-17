# backend/api/api.py
from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from .controllers import (
    create_content, get_all_content, get_content_by_id,
    update_content, delete_content
)

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# ---- Admin can CRUD ----
class AdminContentResource(Resource):
    def post(self):
        """Create new Invincible content"""
        data = request.get_json()
        content = create_content(data)
        return jsonify(content.to_dict()), 201

    def put(self):
        """Update existing content"""
        data = request.get_json()
        item_id = data.get("id")
        updated = update_content(item_id, data)
        return jsonify(updated.to_dict()) if updated else ({"error": "Not found"}, 404)

    def delete(self):
        """Delete content"""
        data = request.get_json()
        item_id = data.get("id")
        deleted = delete_content(item_id)
        return ({"message": "Deleted"} if deleted else {"error": "Not found"}), 200


# ---- User can only view ----
class PublicContentResource(Resource):
    def get(self):
        """Get all Invincible content"""
        return jsonify(get_all_content())


class SinglePublicResource(Resource):
    def get(self, item_id):
        """Get single content by ID"""
        item = get_content_by_id(item_id)
        return jsonify(item) if item else ({"error": "Not found"}, 404)


# Register routes
api.add_resource(AdminContentResource, "/admin/content")
api.add_resource(PublicContentResource, "/content")
api.add_resource(SinglePublicResource, "/content/<int:item_id>")
