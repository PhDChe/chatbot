# -*- coding: utf-8 -*-


class BaseFactsStorage(object):
    """
    Класс описывает контракт для классов, обеспечивающих чтение
    фактов из произвольного хранилища и (опционально) сохранение
    новых фактов. Производные классы могут читать факты из текстовых
    файлов, из базы данных, из веб-сервиса и так далее, и сохранять
    новые факты только в памяти, либо на диске etc.
    """

    INTERCOLUTOR_GENDER_FACT = '<<<interlocutor_gender>>>'

    def __init__(self):
        pass

    def enumerate_facts(self, interlocutor):
        """
        :param interlocutor - строковый идентификатор пользователя,
         используемый при чтении приватных фактов, релевантных только заданному
         пользователю.
        :return итерируемая последовательность кортежей (тест_факта, грамматическое_лицо, уникальная_метка_факта)
        """
        raise NotImplementedError()

    def enumerate_smalltalk_replicas(self):
        """
        :return: итерируемая последовательность экземпляров класса SmalltalkReplicas.
        """
        raise NotImplementedError()

    def store_new_fact(self, interlocutor, fact):
        """
        К списку фактов добавляется новый, полученный в результате
        диалога с пользователем. В зависимости от реализации хранилища
        факт может быть запомнен либо только в памяти, либо сохранен
        в файлах, БД etc
        :param interlocutor: уникальный строковый идентификатор пользователя
        :param fact: строковое представление добавляемого факта
        """
        assert(len(unicode(fact)) > 0)
        raise NotImplementedError()
