import re
from logger import logging

logger = logging.getLogger()

def _read_input_file(path):
    try:
        with open(path, 'r') as fp:
            file = fp.read()
    except:
        exit("Error on reading file!")
    return file


def _clean_input_file(file):
    file = re.sub(r'#.*', '', file)
    file = re.sub(r'^\n', '', file, flags=re.M)
    file = re.sub(r'(?: +$)|(?:^ +)', '', file, flags=re.M)
    file = re.sub(r' +', ' ', file)
    return file


def _parse_input_file(file):
    lines = file.split('\n')
    lines.remove('')
    tab = []

    #getting size
    try:
        size = int(lines[0])
    except:
        exit("Not a valid size!")

    #checking size
    if len(lines[1:]) != size:
        exit("Bad size!")

    #getting all digits
    for line in lines[1:]:
        nums = line.split(' ')
        if len(nums) != size:
            exit("Bad size!")
        if not line.replace(' ', '').isdigit():
            exit("Bad npuzzle!")
        tab.append([int(num) for num in nums])
    return tab


def parse_file(path):
    file = _read_input_file(path)
    logger.info('FILE :\n%s', file)

    cleaned_file = _clean_input_file(file)
    logger.info('CLEANED FILE :\n%s', cleaned_file)

    parsed_file = _parse_input_file(cleaned_file)
    logger.info('PARSED FILE :\n%s', parsed_file)

    return parsed_file
