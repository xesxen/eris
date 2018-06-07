""" Base module for bot modules. """

from eris.events.handler import EventHandler, PRIO_HIGH, PRIO_MEDIUM, PRIO_LOW
from discord.client import Client

class ModuleBase(object):

    """ Modules should always implement a few methods that lets us do what we need to register events. """

    eventhandler: EventHandler = None
    default_priority: int = PRIO_LOW
    client: Client = None

    def register(self):
        """ Register events with the eventhandler """
        raise NotImplementedError("This method has not been implemented on this module")

    def unregister(self):
        """ Deregister the events with the eventhandler. """
        raise NotImplementedError("This method has not been implemented on this module")

    def register_hook(self, hook):
        """ Register a hook with the eventhandler """
        self.eventhandler.register_handler(str(self.__class__), self.default_priority, hook)