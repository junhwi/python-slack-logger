python-slack-logger
===================
.. image:: https://img.shields.io/pypi/pyversions/slack-logger.svg?maxAge=2592000?style=flat-square
    :target: https://pypi.python.org/pypi/slack-logger

Python logging handler for Slack web hook integration with simple configuration.

Installation
------------
.. code-block:: bash

    pip install slack-logger

Example
-------
Simple
''''''
.. code-block:: python

  import logging
  from slack_logger import SlackHandler, SlackFormatter

  sh = SlackHandler('YOUR_WEB_HOOK_URL') # url is like 'https://hooks.slack.com/...'
  sh.setFormatter(SlackFormatter())
  logging.basicConfig(handlers=[sh])
  logging.warning('warn message')

Using logger
''''''''''''
.. code-block:: python

  import logging
  from slack_logger import SlackHandler, SlackFormatter

  logger = logging.getLogger(__name__)
  logger.setLevel(logging.DEBUG)

  sh = SlackHandler(username='logger', icon_emoji=':robot_face:', url='YOUR_WEB_HOOK_URL')
  sh.setLevel(logging.DEBUG)

  f = SlackFormatter()
  sh.setFormatter(f)
  logger.addHandler(sh)

  logger.debug('debug message')
  logger.info('info message')
  logger.warn('warn message')
  logger.error('error message')
  logger.critical('critical message')
