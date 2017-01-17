import logging,requests

logger = logging.getLogger('')

class web2com():

    def __init__(self, core, url, cycle, **kwargs):
        self._cd = core
        self.url = 'http://{}/ws'.format(ip)
        self.items = {}
        core.scheduler.add('_web2com_wr', self.update, cycle=int(cycle))

    def run(self):
        self.alive = True

    def stop(self):
        self.alive = False

    def update(self):
        try:
            XXX
        except Exception as e:
            logger.warning('web2com: could not connect to web2com-Server: {}'.format(e))
            return

