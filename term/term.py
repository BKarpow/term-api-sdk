from core import TermCore
from loguru import logger

logger.add('debug_term.log', format='{time} {level} {message}', level='DEBUG')

class Term(TermCore):

    def __init__(self):
        super(Term, self).__init__()
        self.logging = True
        pass

    def BattaryStatus(self):
        cmd = self.getComands('battery')
        self.commandExecute(cmd)
        

    @logger.catch
    def FingerPrint(self):
        if self.logging:
            logger.info('FingerPrint')
        c = self.getComands('fingerptint')
        res = self.commandExecute(c)
        if len(res['errors']) == 0 and res['auth_status'] == "AUTH_RESULT_SUCCESS":
            return (True, res['failed_attempts'])
        else:
            return (False, res['failed_attempts'], res['errors'])



if __name__ == '__main__':
    logger.info('Battary status test.')
    TApi = Term()
    TApi.debug_trigger()
    TApi.BattaryStatus()
    print(TApi.FingerPrint())
