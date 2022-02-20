#!/usr/bin/env python3
import os

class Config(object):
	SECRET_KY = os.environ.get("SECRET_KEY") or "secret_string"
	