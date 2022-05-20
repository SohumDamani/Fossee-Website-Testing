# Generated by Django 4.0.4 on 2022-05-20 16:14

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0003_alter_homepage_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('navbar_visible', models.BooleanField(default=True)),
                ('sidebar_visible', models.BooleanField(default=True)),
                ('footer_visible', models.BooleanField(default=True)),
                ('content', wagtail.fields.StreamField([('textcontent', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=250, required=True)), ('content', wagtail.blocks.RichTextBlock(required=True))]))], blank=True, null=True, use_json_field=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='footer',
            field=wagtail.fields.StreamField([('contents', wagtail.blocks.StructBlock([('title', streams.blocks.CharBlock()), ('content', wagtail.blocks.RichTextBlock(label='Message'))])), ('extlinks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=250, required=True)), ('links', wagtail.blocks.StreamBlock([('link', wagtail.blocks.StructBlock([('link', wagtail.blocks.RichTextBlock(features=['link'], required=True)), ('visible', wagtail.blocks.BooleanBlock(default=True, required=False))]))]))], icon='link', label='External Links'))], blank=True, null=True, use_json_field=None),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='navbar',
            field=wagtail.fields.StreamField([('navs', wagtail.blocks.StreamBlock([('links', wagtail.blocks.StructBlock([('link', wagtail.blocks.RichTextBlock(features=['link'], required=True)), ('visible', wagtail.blocks.BooleanBlock(default=True, required=False))]))], icon='link'))], blank=True, null=True, use_json_field=None),
        ),
    ]
