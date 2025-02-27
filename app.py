from ekn.database import DatabaseManager
from ekn.routes import (
    categories,
    change_security,
    gdpr_view,
    get_score,
    get_current_key,
    get_vote_count,
    misc,
    register_connection,
    register_service,
    register_user,
    registration,
    users,
    verify_credentials_route,
    version,
    vote,
)
from flask import Flask


DatabaseManager()  # Update DB
app = Flask(__name__)


app.add_url_rule("/categories", view_func=categories, methods=["GET", "OPTIONS"])
app.add_url_rule(
    "/change_security", view_func=change_security, methods=["POST", "OPTIONS"]
)
app.add_url_rule(
    "/change_password", view_func=users.change_password, methods=["POST", "OPTIONS"]
)
app.add_url_rule("/gdpr_view", view_func=gdpr_view, methods=["POST", "OPTIONS"])
app.add_url_rule("/get_score", view_func=get_score, methods=["POST", "OPTIONS"])
app.add_url_rule(
    "/get_current_key", view_func=get_current_key, methods=["POST", "OPTIONS"]
)
app.add_url_rule(
    "/get_vote_count", view_func=get_vote_count, methods=["POST", "OPTIONS"]
)
app.add_url_rule(
    "/get_total_users", view_func=misc.get_total_users, methods=["GET", "OPTIONS"]
)
app.add_url_rule(
    "/get_total_real_users",
    view_func=misc.get_total_real_users,
    methods=["GET", "OPTIONS"],
)
app.add_url_rule(
    "/get_total_temp_users",
    view_func=misc.get_total_temp_users,
    methods=["GET", "OPTIONS"],
)
app.add_url_rule(
    "/get_total_votes", view_func=misc.get_total_votes, methods=["GET", "OPTIONS"]
)
app.add_url_rule(
    "/register_connection", view_func=register_connection, methods=["POST", "OPTIONS"]
)
app.add_url_rule(
    "/register_service", view_func=register_service, methods=["POST", "OPTIONS"]
)
app.add_url_rule(
    "/register_temp_user",
    view_func=registration.register_temp_user,
    methods=["POST", "OPTIONS"],
)
app.add_url_rule("/register_user", view_func=register_user, methods=["POST", "OPTIONS"])
app.add_url_rule(
    "/verify_credentials",
    view_func=verify_credentials_route,
    methods=["POST", "OPTIONS"],
)
app.add_url_rule("/version", view_func=version, methods=["GET"])
app.add_url_rule("/vote", view_func=vote, methods=["POST", "OPTIONS"])
