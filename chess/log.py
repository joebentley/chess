from datetime import datetime

logfile = open('log', 'w')

def log(message):
    """Log the string message to output file with a timestamp."""
    logfile.write('[' + datetime.now().isoformat(' ') + ']: ' + message + '\n')
