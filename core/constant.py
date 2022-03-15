import os
import inspect


class Constant:
    # GitHub user name
    USERNAME = 'Eurus-Holmes'

    # The amount of tasks to each every day
    CRON_CONFIG = {
        'Easy': 0,
        'Medium': 1,
        'Hard': 2,
    }

    ROOT_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../'

    RES_PATH = ROOT_PATH + 'res/'

    QUESTIONS_PATH = RES_PATH + 'leetcode-questions.json'

    SOLUTIONS_PATH = RES_PATH + 'solutions/'

    BUILD_PATH = ROOT_PATH + 'build/'
