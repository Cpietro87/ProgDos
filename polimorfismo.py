class Notificacion:
    def enviar(self):
        pass


class Email(Notificacion):
    def enviar(self):
        return "Enviando email"


class SMS(Notificacion):
    def enviar(self):
        return "Enviando SMS 📱"


class Push(Notificacion):
    def enviar(self):
        return "Enviando notificación push"
    
class WhatsApp(Notificacion):
    def enviar(self):
        return "Enviando mensaje de WhatsApp"

class Telegram(Notificacion):
    def enviar(self):
        return "Enviando mensaje de Telegram"
    

notificaciones = [Email(), SMS(), Push(), WhatsApp(), Telegram()]
for n in notificaciones:
    print(n.enviar())

