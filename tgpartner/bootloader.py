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
import importlib.util
import sys
import os
import logging

logger = logging.getLogger()


async def send_success_message(client):
    text = "Hello!! Your tgpartner has been started successfully."
    await client.send_message("me", text)


def load_module(client, file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    module.client = client
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


async def load_plugins(client):
    await load_general_plugins(client)
    await load_fun_plugins(client)


async def load_general_plugins(client):
    for file in os.listdir("tgpartner/plugins/general"):
        if file.startswith("_"):
            continue
        path = os.path.join(os.path.realpath("tgpartner/plugins/general"), file)
        name = file.replace(".py", "")
        try:
            load_module(client, path, name)
            print("Loaded plugin ", name)
        except ModuleNotFoundError:
            try:
                os.system("pip3 install -r requirements.txt")
                load_module(client, path, name)
                print("Loaded plugin ", name)
            except Exception as e:
                print(e)
        except Exception as e:
            print("Unable to load ", name, e)


async def load_fun_plugins(client):
    for file in os.listdir("tgpartner/plugins/fun"):
        if file.startswith("_"):
            continue
        path = os.path.join(os.path.realpath("tgpartner/plugins/fun"), file)
        name = file.replace(".py", "")
        try:
            load_module(client, path, name)
            print("Loaded plugin ", name)
        except ModuleNotFoundError:
            try:
                os.system("pip3 install -r requirements.txt")
                load_module(client, path, name)
                print("Loaded plugin ", name)
            except Exception as e:
                print(e)
        except Exception as e:
            print("Unable to load ", name, e)


async def load_core_files(client):
    for file in os.listdir("tgpartner/core"):
        if file.startswith("_"):
            continue
        path = os.path.join(os.path.realpath("tgpartner/core"), file)
        name = file.replace(".py", "")
        load_module(client, path, name)
