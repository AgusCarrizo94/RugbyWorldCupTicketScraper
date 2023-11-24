import pywhatkit

def whatsAppMessage(message):
    pywhatkit.sendwhatmsg_to_group_instantly("CHATCODE", message, tab_close=True)
