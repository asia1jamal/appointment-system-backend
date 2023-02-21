"""from channels.routing import route
from doctor import consumer


channel_routing = {
    route(' chatt.connect',consumer.ws_add),
    route('chatt.receive',consumer.ws_messages),
    route('chatt.disconnect',consumer.ws_disconnect),
}"""