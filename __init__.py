from mycroft import MycroftSkill, intent_file_handler


class Musculacao(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('musculacao.intent')
    def handle_musculacao(self, message):
        self.speak_dialog('musculacao')


def create_skill():
    return Musculacao()

