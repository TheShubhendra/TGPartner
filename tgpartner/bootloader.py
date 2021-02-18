async def send_success_message(client):
    text = "Hello!! Your tgpartner has been started successfully."
    await client.send_message("me", text)
