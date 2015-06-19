import bottle
import logging
from app import Beer, settings


logger = logging.Logger(__name__)


def main():
    logger.info('Beer started')
    beer = Beer(
        debug=settings.DEBUG,
        reloader=settings.RELOADER,
        logging_config=settings.LOGGING)
    bottle.run(
        beer.app,
        server=beer.server,
        host=beer.host,
        port=beer.port,
        reloader=beer.reloader)

if __name__ == '__main__':
    main()
