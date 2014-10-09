
# Simple SMTP Proxy #

  smtpproxyd is a simple service application that proxies non-authed SMTP mail
  to authed SMTP servers using SSL/TLS.

  Many old legacy applications use non modifiable mail sending libraries which
  use simple SMTP. It is now frequent to delegate this tasks to third party
  authenticated SMTPs.

## Installation ##
```
pip install --pre smtpproxyd
```

  Three commands are supported:
  - **listen** Will setup a local unauthed SMTP service wich will listen on provided HOST and PORT, proxying 
    all mail using the provided remote SMTP information.
  - **testupsteamsmtp** Will test the remote SMTP communication sending a test mail.
  - **testlocalsmtp** Will test a local server started using the listen command.

```
  Usage:
    smtpproxyd listen [options] <remote-host> <remote-username>
    smtpproxyd testupstreamsmtp [options] -r EMAIL <remote-host> <remote-username>
    smtpproxyd testlocalsmtp [options] -r EMAIL

  Options:
    -h HOST --host HOST         Host [default: 127.0.0.1] on which the local
                                SMTP server will run.  Note that you should
                                trust all users on the host, and you should
                                not run this on public interfaces as this would
                                create an open relay straight through your
                                authed SMTP provider.
    -p PORT --port=PORT         Port [default: 1025] on which smtpproxyd will
                                listen.
    -P PORT --remote-port=PORT  Remote SMTP service port [default: 587].
    -r EMAIL --rcpt=EMAIL       Email address of test recipient.
```
