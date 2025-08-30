from .routing import router
__all__ = ["router"]
# This makes the router accessible when importing from the events package
# This file initializes the events package and makes the router accessible
# when importing from the events package.
# It allows other parts of the application to include the event-related routes easily.
# By including this __init__.py file, we can import the router directly from the events package.
# For example, from api.events import router
# This is useful for organizing the code and keeping the routing logic modular.