from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io_template import CheckiOReferee
from checkio.referees import cover_codes

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            "python": "mult_two",
            "js": "multTwo"
        },
        cover_code={
            'python-3': {},
            'js-node': {
                # "dateForZeros": True,
            }
        }
    ).on_ready)
