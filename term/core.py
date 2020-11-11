import subprocess
import json

from loguru import logger

logger.add('debug_core.log', format='{time} {level} {message}', level='DEBUG')

class TermCore:
    def __init__(self):
        self.debug = False
        self.raw_output = ''
        self.error = ''
        self.return_code = 0
        self.prefix = 'termux-'
        self.commands = {
            'battery': self.prefix + 'battry-status',
            'fingerprint': self.prefix + 'fingerprint',
            'wifi-scan': self.prefix + 'wifi-scan'
            
        }



    def debug_trigger(self):
        self.debug = not(self.debug)
        if  (self.debug):
            logger.info("Debug-mode enable!")
        else:
            logger.info("Debug-mode disable!")


    def getComands(self, command):
        if (self.commands.get(command) != None):
            return self.commands[command]
        else:
            logger.error(f'Command {command} not found!');
            return None

    @logger.catch
    def commandExecute(self, cmd, encoding='UTF-8', timeout=None, shell=False):
        proc = subprocess.Popen(cmd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=shell)
        output, error = proc.communicate(timeout=timeout)
        output = output.decode(encoding).rstrip()
        error = error.decode(encoding).rstrip()
        rc = proc.returncode
        self.return_code = rc
        if self.debug:
            logger.debug('Returncode: ' + str(rc))
            logger.debug('Error: ' + str(error))
            logger.debug('Raw output: ' + str(output))
        self.raw_output = output
        self.error = error
        return json.loads(output)