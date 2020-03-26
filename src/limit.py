from flask_limiter import Limiter

limiter = Limiter()

@limiter.limit('20/hour', exempt_when=admin_conditions)
def init_app(app):
    limiter.init_app(app)
