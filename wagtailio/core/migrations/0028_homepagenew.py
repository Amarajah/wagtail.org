# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-14 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtailio.utils.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('images', '0002_update_to_wagtail_13'),
        ('core', '0027_update_to_wagtail_13'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageNew',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, help_text='Description of this page as it should appear when shared on social networks, or in Google results', max_length=255, verbose_name='Meta description')),
                ('listing_intro', models.TextField(blank=True, help_text='Summary of this page to display when this is linked from elsewhere in the site.')),
                ('introduction', models.CharField(max_length=511)),
                ('body', wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('blockquote', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='openquote')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('imagecaption', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock())), label='Image caption')), ('textimage', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock()), ('alignment', wagtailio.utils.blocks.SimpleImageFormatChoiceBlock())), icon='image')), ('colourtext', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())), icon='pilcrow')), ('calltoaction', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())), icon='pilcrow')), ('tripleimage', wagtail.wagtailcore.blocks.StructBlock((('first_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('second_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('third_image', wagtail.wagtailimages.blocks.ImageChooserBlock())), icon='image')), ('stats', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('stat', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.CharBlock())), icon='code'))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='code')), ('markdown', wagtailio.utils.blocks.MarkDownBlock()), ('codeblock', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('django', 'Django templating language'), ('html', 'HTML'), ('javascript', 'Javascript'), ('python', 'Python'), ('scss', 'SCSS')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
                ('listing_image', models.ForeignKey(blank=True, help_text='Image to display along with summary, when this page is linked from elsewhere in the site.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.WagtailIOImage')),
                ('social_image', models.ForeignKey(blank=True, help_text="Image to appear alongside 'Meta descro[topm', particularly for sharing on social networks", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.WagtailIOImage', verbose_name='Meta image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
