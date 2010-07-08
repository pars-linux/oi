from django import template
from django.core.urlresolvers import reverse



register = template.Library()
@register.inclusion_tag('beyin2/tt_idea_vote.html')
def is_voted(idea, user):
    vote = idea.vote_set.filter( voter=user )
    if vote:
        return {'idea':idea,'vote':vote[0].vote}
        #if not exist send Y
    else:
        return {'idea':idea,'vote': "Y"}

