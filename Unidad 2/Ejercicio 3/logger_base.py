import logging as log

log.basicConfig(
    level=log.DEBUG, 
    format="%(asctime)s | %(levelname)s | [%(filename)s] en linea %(lineno)s | Mensaje: [%(message)s].",
    datefmt="%I:%M:%S %p",
    handlers=[
        log.FileHandler('Logging.log'),
        log.StreamHandler()
    ]
);

if __name__ == '__main__':
    log.debug('Prueba de logeo.')
