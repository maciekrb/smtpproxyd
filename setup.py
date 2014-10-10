from distutils.core import setup
import sys

if float("%d.%d" % sys.version_info[:2]) < 2.4:
  sys.stderr.write(('Your Python version %d.%d.%d '
                    'is not supported.\n') % sys.version_info[:3])
  sys.stderr.write("smtpproxy requires Python 2.4 or newer.\n")
  sys.exit(1)

## Main distutils info
setup(
  ## Content description
  name='smtpproxyd',
  version='0.2-alpha',
  scripts=['smtpproxyd'],

  ## Packaging details
  author="Maciek Ruckgaber",
  author_email="maciekrb@gmail.com",
  license='GPL version 2',
  description='Simple SMTP proxy',
  long_description="""
smtpproxy provides a simple daemon that can forward unauthed
SMTP connections to authenticated SMTP servers. It is a convenience
service for old legacy software that can't be modified for sending
email through authenticated SMTP.

Authors:
--------
    Maciek Ruckgaber  <maciekrb@gmail.com>
""",
  install_requires=["docopt"]
)
