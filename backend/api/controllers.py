# backend/api/controllers.py
from .models import InvincibleContent
from .db import db

def create_content(data):
    new_item = InvincibleContent(
        title=data["title"],
        description=data["description"],
        image_filename=data["image_filename"],
        category=data.get("category", "General")
    )
    db.session.add(new_item)
    db.session.commit()
    return new_item

def get_all_content():
    return [item.to_dict() for item in InvincibleContent.query.order_by(InvincibleContent.created_at.desc()).all()]

def get_content_by_id(item_id):
    item = InvincibleContent.query.get(item_id)
    return item.to_dict() if item else None

def update_content(item_id, data):
    item = InvincibleContent.query.get(item_id)
    if item:
        item.title = data.get("title", item.title)
        item.description = data.get("description", item.description)
        item.image_filename = data.get("image_filename", item.image_filename)
        item.category = data.get("category", item.category)
        db.session.commit()
        return item
    return None

def delete_content(item_id):
    item = InvincibleContent.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return True
    return False
