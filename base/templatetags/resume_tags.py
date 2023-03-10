from django import template

from ..models import Experience

register = template.Library()


@register.inclusion_tag('base/experience-item.html')
def show_experience(side):
    experiences = Experience.objects.all()
    experience = []
    if side == 'left':
        for i in range(0, len(experiences) // 2 + len(experiences) % 2):
            experience.append(experiences[i])
    elif side == 'right':
        for i in range(len(experiences) // 2 + len(experiences) % 2, len(experiences)):
            experience.append(experiences[i])
    return {'experience': experience}
