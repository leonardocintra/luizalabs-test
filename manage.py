import bottle
from logging import info
from app import Beer, settings


def main():
    info('Beer started')
    beer = Beer(
        debug=settings.DEBUG,
        reloader=settings.RELOADER)
    bottle.run(
        beer.app,
        server=beer.server,
        host=beer.host,
        port=beer.port,
        reloader=beer.reloader)

if __name__ == '__main__':
    main()
