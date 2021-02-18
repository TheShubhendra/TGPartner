import importlib.util
import sys
import os
import logging

logger = logging.getLogger()
async def send_success_message(client):
    text = "Hello!! Your tgpartner has been started successfully."
    await client.send_message("me", text)


def load_module(client, file_path, module_name):
    print("Loading", module_name)
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    module.client = client
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


async def load_plugins(client):
    for file in os.listdir("tgpartner/plugins"):
        if file.startswith("_"):
            continue
        path = os.path.join(os.path.realpath("tgpartner/plugins"), file)
        name = file.replace(".py","")
        load_module(client, path, name)
