# Generated by Django 4.0.4 on 2022-05-19 16:21

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='footer',
            field=wagtail.fields.StreamField([('footer', wagtail.blocks.StructBlock([('extlink', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=250, required=True)), ('links', wagtail.blocks.StreamBlock([('link', wagtail.blocks.StructBlock([('link', wagtail.blocks.RichTextBlock(features=['link'], required=True)), ('visible', wagtail.blocks.BooleanBlock(default=True, required=False))]))]))])), ('title', streams.blocks.CharBlock()), ('content', wagtail.blocks.TextBlock())]))], blank=True, null=True, use_json_field=None),
        ),
    ]
