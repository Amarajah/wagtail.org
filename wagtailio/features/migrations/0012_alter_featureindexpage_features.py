# Generated by Django 3.2.12 on 2022-08-31 07:46

from django.db import migrations

import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        (
            "features",
            "0011_featureindexpage_rename_body_to_features_add_subheading_cta_get_started",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="featureindexpage",
            name="features",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "features",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "blocks",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.core.blocks.CharBlock(
                                                        max_length=255
                                                    ),
                                                ),
                                                (
                                                    "features",
                                                    wagtail.core.blocks.ListBlock(
                                                        wagtail.core.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "heading",
                                                                    wagtail.core.blocks.CharBlock(
                                                                        label="Feature heading",
                                                                        max_length=255,
                                                                        required=False,
                                                                    ),
                                                                ),
                                                                (
                                                                    "description",
                                                                    wagtail.core.blocks.RichTextBlock(
                                                                        features=[
                                                                            "bold",
                                                                            "italic",
                                                                            "link",
                                                                            "document",
                                                                        ],
                                                                        label="Feature description",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                                (
                                                                    "link",
                                                                    wagtail.core.blocks.URLBlock(
                                                                        label="Feature link",
                                                                        required=False,
                                                                    ),
                                                                ),
                                                                (
                                                                    "link_title",
                                                                    wagtail.core.blocks.CharBlock(
                                                                        default="View docs",
                                                                        label="Feature link title",
                                                                        max_length=50,
                                                                        required=False,
                                                                    ),
                                                                ),
                                                            ]
                                                        ),
                                                        min_num=2,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    )
                ],
                blank=True,
            ),
        ),
    ]
