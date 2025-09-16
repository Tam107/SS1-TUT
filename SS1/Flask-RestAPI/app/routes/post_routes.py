from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.post import Post
from ..extensions import db
from ..schemas.post_schema import PostSchema

post_bp = Blueprint("posts", __name__)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)


@post_bp.route("/", methods=["GET"])
def get_posts():
    # --- Lấy query params ---
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)
    sort_by = request.args.get("sort_by", "created_at", type=str)
    order = request.args.get("order", "desc", type=str)
    search = request.args.get("search", "", type=str)

    # --- Tạo query gốc ---
    query = Post.query

    # --- Search ---
    if search:
        query = query.filter(
            (Post.title.ilike(f"%{search}%")) | (Post.content.ilike(f"%{search}%"))
        )

    # --- Sorting ---
    if sort_by not in ["created_at", "title"]:
        sort_by = "created_at"

    sort_column = getattr(Post, sort_by)
    if order == "desc":
        sort_column = sort_column.desc()
    else:
        sort_column = sort_column.asc()

    query = query.order_by(sort_column)

    # --- Pagination ---
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "items": posts_schema.dump(pagination.items),
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages,
        "per_page": pagination.per_page
    })


@post_bp.route("/", methods=["POST"])
@jwt_required()
def create_post():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_post = Post(title=data["title"], content=data["content"], user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return post_schema.jsonify(new_post), 201
