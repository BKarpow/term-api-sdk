from core import TermCore
from loguru import logger

logger.add('debug_term.log', format='{time} {level} {message}', level='DEBUG')

class Term(TermCore):

    def __init__(self):
        super(Term, self).__init__()
        pass

    def BattaryStatus(self):
        cmd = self.getComands('battery')
        self.commandExecute(cmd)
        logger.info('Command Ececute: ' + cmd)


if __name__ == '__main__':
    logger.info('Battary status test.')
    TApi = Term()
    TApi.debug_trigger()
    TApi.BattaryStatus()
