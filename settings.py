# coding: utf8
import os
import yaml

if os.path.exists(os.path.dirname(__file__) + "/yaml/config.yml"):
    env = os.environ.get('env', 'production')
    env = env.lower()
    if env in ['production']:
        CONFIG = yaml.safe_load(open(os.path.dirname(__file__) + "/yaml/config.yml", 'r'))[env]
        TEST_DATA = yaml.safe_load(open(os.path.dirname(__file__) + "/yaml/{}.yml".format(env)))
    else:
        raise("Invalid Environment")
else:
    raise("config.yml does not exists")

platform = (CONFIG['platform'])