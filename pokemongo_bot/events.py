

class EventNotRegisteredException(Exception):
    pass


class EventMalformedException(Exception):
    pass


class EventHandler:
    def __init__(self):
        pass

    def handle_event(self, event, kwargs):
        raise NotImplementedError("Please implement")


class EventManager:
    def __init__(self):
        self._registered_events = dict()
        self._handlers = []

    def add_handler(self, event_handler):
        self._handlers.append(event_handler)

    def register_event(self, name, parameters=None):
        self._registered_events[name] = parameters

    def emit(self, event, **kwargs):
        if event not in self._registered_events:
            raise EventNotRegisteredException("Event %s not registered..." % event)

        # verify params match event
        parameters = self._registered_events[event]
        for k, v in kwargs.iteritems():
            if k not in parameters:
                raise EventMalformedException("Event %s does not have parameter %s" % (event, k))

        # send off to the handlers
        for handler in self._handlers:
            handler.handle_event(event, kwargs)
