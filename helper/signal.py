from django.core.signals import request_finished
from django.core.signals import request_started
from django.test.signals import template_rendered
from django.dispatch import receiver

#request_finished.connect(my_callback)
@receiver(template_rendered)
def my_template_rendered(sender, **kwargs):
    #print(sender)
    #print(kwargs)
    print("template rendered!")

@receiver(request_started)
def my_request_started(sender, **kwargs):
    #print(sender)
    #print(kwargs)
    print("Request started!")

@receiver(request_finished)
def my_request_finished(sender, **kwargs):
    #print(sender)
    #print(kwargs)
    print("Request finished!")