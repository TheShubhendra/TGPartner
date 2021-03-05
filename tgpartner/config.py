#!/usr/bin/python
# A telegram bot that works parallel with you
# and provide additional interface and unlimited features.
# Copyright (C) 2021 Shubhendra Kushwaha
# @TheShubhendra shubhendrakushwaha94@gmail.com
# This file is a part of TGPartner <https://github.com/TheShubhendra/TGPartner>.
#
# TGPartner is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TGPartner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TGPartner.  If not, see <http://www.gnu.org/licenses/>.
from decouple import config


ENV = config("ENV", "development")
APP_ID = config("APP_ID")
API_HASH = config("API_HASH")


# Production variables
APP_NAME = config("APP_NAME", None)
STRING_SESSION = config("STRING_SESSION", None)
REPO_URL = config("REPO_URL", "https://GitHub.com/TheShubhendra/TGPartner")
LOGGING_LEVEL = int(config("LOGGING_LEVEL", 30))
