import argparse
import datetime
import json
import logging
import os
import requests
import requests.utils
import stat
import sys
import time

import module.qoj
import module.codeforces

adapter = None

