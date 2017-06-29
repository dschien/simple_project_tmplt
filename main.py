import numpy as np

import itertools
import configparser

CONFIG_FILE = "local.cfg"
cfg = configparser.ConfigParser()
cfg.read_file(itertools.chain(['[global]'], open(CONFIG_FILE)))
config = cfg['global']
