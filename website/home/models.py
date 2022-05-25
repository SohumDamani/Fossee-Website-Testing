from django.db import models
from django import forms

from modelcluster.fields import ParentalManyToManyField

from streams import blocks

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

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

@register_snippet
class Navbar(models.Model):
    title = models.CharField(unique=True,max_length=255)
    logo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.CASCADE, related_name='+'
    )
    links = StreamField([
        ('navs',blocks.LinkBlock())
    ],null=True,blank=True)

    panels = [FieldPanel('title'),
              ImageChooserPanel('logo'),
              FieldPanel('links',heading='Nav Links',classname='collapsible')]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Navbar"
        verbose_name_plural = "Navbars"

@register_snippet
class Sidebar(models.Model):
    title = models.CharField(unique=True,max_length=255)
    sidebar = StreamField(
        [
            ('sidebar',blocks.SidebarBlock())
        ],null=True,blank=True)
    panels = [FieldPanel('title'),
              FieldPanel('sidebar')]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sidebar"
        verbose_name_plural = "Sidebars"

@register_snippet
class Footer(models.Model):
    title = models.CharField(unique=True,max_length=255)
    footer = StreamField(
        [
            ('contents', blocks.FooterBlock()),
            ('extlinks',blocks.SidebarBlock(label='External Links',icon='link'))
        ],null=True,blank=True)

    panels = [FieldPanel('title'),
              FieldPanel('footer')]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"


class TestPage(Page):
    navbar = ParentalManyToManyField(Navbar,null=True,blank=True)
    sidebar = ParentalManyToManyField(Sidebar,null=True,blank=True)
    footer = ParentalManyToManyField(Footer,null=True,blank=True)

    content_panels = Page.content_panels+[
        FieldPanel('navbar',widget=forms.CheckboxSelectMultiple),
        FieldPanel('sidebar',widget=forms.CheckboxSelectMultiple),
        FieldPanel('footer',widget=forms.CheckboxSelectMultiple),
    ]