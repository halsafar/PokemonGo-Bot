from events import EventHandler


class LoggingHandler(EventHandler):
    def handle_event(self, event, kwargs):
        print "%s:%s" % (event, kwargs)
