from django.db import models

from streams import blocks

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel,FieldRowPanel

class HomePage(Page):

    def get_context(self, request, *args, **kwargs):
        home = HomePage.objects.get(slug='home')
        context = super(HomePage,self).get_context(request)
        context['homepage'] = home
        return context

    max_count = 1


    navbar = StreamField(
        [
            ('navs',blocks.StreamBlock(
                [
                    ('links',blocks.LinkBlock())
                ],icon='link'
            ))
        ],null=True,blank=True,max_num=1)

    sidebar = StreamField(
        [
            ('sidebar',blocks.SidebarBlock())
        ],null=True,blank=True)

    footer = StreamField(
        [
            ('contents', blocks.FooterBlock()),
            ('extlinks',blocks.SidebarBlock(label='External Links',icon='link'))
        ],null=True,blank=True,max_num=4)

    content_panels = Page.content_panels+[
        MultiFieldPanel(
            [
                FieldPanel('navbar'),
                FieldPanel('sidebar'),
                FieldPanel('footer')
            ],heading="Basic Features",
            classname='collapsible'
        )

    ]

class FlexPage(Page):
    def get_context(self, request, *args, **kwargs):
        home = HomePage.objects.get(slug='home')
        context = super(FlexPage,self).get_context(request)
        context['homepage'] = home
        return context

    navbar_visible = models.BooleanField(default=True)
    sidebar_visible = models.BooleanField(default=True)
    footer_visible = models.BooleanField(default=True)

    content = StreamField(
        [
            ('textcontent',blocks.TitleAndContent())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels+[
        MultiFieldPanel([
            FieldPanel('navbar_visible',heading='Navbar'),
            FieldPanel('sidebar_visible',heading='Sidebar'),
            FieldPanel('footer_visible',heading='Footer'),
        ],heading='Basic Features Visibility',
        classname='collapsible collapsed'),
        FieldPanel('content')
    ]

