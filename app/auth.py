from flask import g, redirect, url_for, flash
from functools import wraps


def login_required(f):
    """Used to restrict certain pages without authentication, redirecting to login page if needed"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.current_user:
            flash("Please log in first.")
            return redirect(url_for("goals.login"))

        return f(*args, **kwargs)

    return decorated_function
