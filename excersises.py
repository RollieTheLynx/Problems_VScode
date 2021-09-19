# -*- coding: utf-8 -*-
"""

"""
import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'] = dj_database_url.config(default='postgres://sljaiyeemkopbo:80b6d99c0dff13e1fc7ce32385d90963fea9d9065dad402e07d063fdbcb1d927@ec2-34-253-116-145.eu-west-1.compute.amazonaws.com:5432/d4okmrqc4lb2mh')
DATABASES['default'] = dj_database_url.parse('postgres://sljaiyeemkopbo:80b6d99c0dff13e1fc7ce32385d90963fea9d9065dad402e07d063fdbcb1d927@ec2-34-253-116-145.eu-west-1.compute.amazonaws.com:5432/d4okmrqc4lb2mh', conn_max_age=600)
print(DATABASES['default'])
