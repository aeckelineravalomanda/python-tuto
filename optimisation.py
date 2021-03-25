import sysconfig
print('{}'.format('\n'.join(['{} = {}'.format(v, sysconfig.get_config_var(v)) for v in sorted(sysconfig.get_config_vars(), key=lambda s: s.lower())])))" > /tmp/python3.conf