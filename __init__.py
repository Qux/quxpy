try:
    from .quxpy import event
    from .quxpy import osc_receiver
    from .quxpy import osc_sender
    from .quxpy import simple_event
except ModuleNotFoundError:
    print(" Some modules does not work because the dependencies are not installed collectly.")