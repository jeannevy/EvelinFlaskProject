#!/usr/bin/env python3
import os

class Config(object):
	SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_string"
	MONGODB_SETTINGS = {'db':'Like_poems'}