# backend/api/models.py
from datetime import datetime
from .db import db

class InvincibleContent(db.Model):
    __tablename__ = "invincible_content"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50), nullable=True)  # e.g. 'Character', 'Episode', 'News'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image_filename": self.image_filename,
            "image_url": f"/images/{self.image_filename}",
            "category": self.category,
            "created_at": self.created_at.isoformat()
        }
