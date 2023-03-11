from django import template
from taggit.models import Tag

from ..models import Experience, Project

register = template.Library()


@register.inclusion_tag('base/experience-item.html')
def show_experience(side):
    experiences: list = Experience.objects.all()
    experience: list = []
    if side == 'left':
        for i in range(0, len(experiences) // 2 + len(experiences) % 2):
            experience.append(experiences[i])
    elif side == 'right':
        for i in range(len(experiences) // 2 + len(experiences) % 2, len(experiences)):
            experience.append(experiences[i])
    return {'experience': experience}


@register.inclusion_tag('base/portfolio-item.html')
def project_card():
    tag_list: list = Tag.objects.all()
    # used for list items
    tag_filters: list = []
    for tag in tag_list:
        tag_filters.append({'name': tag.name, 'slug': '.' + tag.slug})
    project_list: list = Project.objects.all()
    project_data: list = []
    for project in project_list:
        project_data.append({'project': project, 'tags': [' ' + ptag for ptag in project.tags.slugs()]})
    return {'tag_filters': tag_filters, 'project_data': project_data}
