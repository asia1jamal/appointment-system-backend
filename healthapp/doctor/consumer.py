"""from channels import Group
#connect
def ws_add(message):
    message.reply_channel.send({'accept':True})
    Group('chatt').add(message.reply_channel)


#receive
def ws_messages(message):
    Group('chatt').send({'text':message.content['text']})


#disconnect
def ws_disconnect(message):
    Group('chatt').discard(message.reply_channel)"""