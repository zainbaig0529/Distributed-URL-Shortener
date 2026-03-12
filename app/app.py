from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from models import db, URLMap
from config import Config
import redis
import random
import string

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
redis_client = redis.Redis.from_url(app.config["REDIS_URL"], decode_responses=True)

with app.app_context():
    db.create_all()

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choices(characters, k=length))
        existing = URLMap.query.filter_by(short_code=short_code).first()
        if not existing:
            return short_code

@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_short_code()

    new_url = URLMap(
        original_url=original_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()

    redis_client.set(short_code, original_url)

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5050/{short_code}",
        "original_url": original_url
    }), 201

@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    cached_url = redis_client.get(short_code)

    if cached_url:
        url_entry = URLMap.query.filter_by(short_code=short_code).first()
        if url_entry:
            url_entry.clicks += 1
            db.session.commit()
        return redirect(cached_url)

    url_entry = URLMap.query.filter_by(short_code=short_code).first()

    if not url_entry:
        return jsonify({"error": "Short URL not found"}), 404

    redis_client.set(short_code, url_entry.original_url)
    url_entry.clicks += 1
    db.session.commit()

    return redirect(url_entry.original_url)

@app.route("/stats/<short_code>", methods=["GET"])
def get_stats(short_code):
    url_entry = URLMap.query.filter_by(short_code=short_code).first()

    if not url_entry:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({
        "original_url": url_entry.original_url,
        "short_code": url_entry.short_code,
        "clicks": url_entry.clicks,
        "created_at": url_entry.created_at.isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)