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
                ]
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

    content_panels = Page.content_panels+[
        MultiFieldPanel(
            [
                FieldPanel('navbar'),
                FieldPanel('sidebar')
            ],heading="Basic Features",
            classname='collapsible'
        )

    ]

