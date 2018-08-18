from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    session_factory1 = SignedCookieSessionFactory(
        'this_is_session_key')
    config = Configurator(settings=settings,
                          session_factory=session_factory1)
    config.include('pyramid_chameleon')
    config.add_route('login', '/')
    config.add_route('slide', '/slide/{page}')
    config.add_route('end',   '/end')
    config.scan('abomid')
    config.add_static_view(name='static', path='images')
    return config.make_wsgi_app()
