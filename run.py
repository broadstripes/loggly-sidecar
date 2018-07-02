import os, sys, re

if('LOGGLY_AUTH_TOKEN' not in os.environ):
    print('Missing $LOGGLY_AUTH_TOKEN')
    sys.exit(1)


if('LOGGLY_TAG' not in os.environ):
    print('Missing $LOGGLY_TAG')
    sys.exit(1)

auth_token = os.environ['LOGGLY_AUTH_TOKEN']

tags = []
for tag in os.environ['LOGGLY_TAG'].split(","):
    tags.append('tag=\\"{}\\"'.format(tag))

with open('/etc/syslog-ng/syslog-ng.conf.tmpl') as conf_template_file:
    conf_template = conf_template_file.read()
    conf = re.sub('LOGGLY_AUTH_TOKEN', auth_token, conf_template)
    conf = re.sub('LOGGLY_TAG', ' '.join(tags), conf)

with open('/etc/syslog-ng/syslog-ng.conf', 'w') as conf_file:
    conf_file.write(conf)

os.execlp('syslog-ng', 'syslog-ng', '--foreground', '--stderr', '--verbose')
