# -*- coding: utf-8 -*-

import logging.handlers, sys

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

formatter = logging.Formatter("""------------
'%(module)s '%(asctime)s.%(msecs)d %(levelname)s  at line %(lineno)d: %(message)s""",
                              '%Y-%m-%d %H:%M:%S')

handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)

handler = logging.FileHandler('scr.log', 'a')
handler.setLevel(logging.WARNING)
handler.setFormatter(formatter)
log.addHandler(handler)

if __name__ == '__main__':
    log.exception()