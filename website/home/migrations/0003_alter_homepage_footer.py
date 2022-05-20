# Generated by Django 4.0.4 on 2022-05-19 16:25

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='footer',
            field=wagtail.fields.StreamField([('footer', wagtail.blocks.StructBlock([('title', streams.blocks.CharBlock()), ('content', wagtail.blocks.TextBlock())])), ('extlinks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=250, required=True)), ('links', wagtail.blocks.StreamBlock([('link', wagtail.blocks.StructBlock([('link', wagtail.blocks.RichTextBlock(features=['link'], required=True)), ('visible', wagtail.blocks.BooleanBlock(default=True, required=False))]))]))]))], blank=True, null=True, use_json_field=None),
        ),
    ]