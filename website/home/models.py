from django.db import models

from streams import blocks

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel

class HomePage(Page):
    navbar = StreamField(
        [
            ('navs',blocks.StreamBlock(
                [
                    ('links',blocks.LinkBlock())
                ],icon='link'
            ))
        ],
        null=True,
        blank=True,
        max_num=1
    )
    sidebar = StreamField(
        [
            ('sidebar',blocks.SidebarBlock())
        ],
        null=True,
        blank=True
    )
    footer = StreamField(
        [
            ('contents', blocks.FooterBlock()),
            ('extlinks',blocks.SidebarBlock(label='External Links',icon='link'))
        ],
        null=True,
        blank=True,
        max_num=4
    )

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

