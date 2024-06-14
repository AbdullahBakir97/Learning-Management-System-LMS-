# Generated by Django 5.0.6 on 2024-06-13 20:18

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("activity", "0003_initial"),
        ("certifications", "0004_initial"),
        ("courses", "0002_initial"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="instructed_courses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="reactions",
            field=models.ManyToManyField(
                blank=True, related_name="course_reactions", to="activity.reaction"
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="shares",
            field=models.ManyToManyField(
                blank=True, related_name="course_shares", to="activity.share"
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="coursecompletion",
            name="certificate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="course_completions",
                to="certifications.certification",
            ),
        ),
        migrations.AddField(
            model_name="coursecompletion",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="completions",
                to="courses.course",
            ),
        ),
        migrations.AddField(
            model_name="coursecompletion",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="completed_courses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="coursecompletion",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="courseenrollment",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrolled_courses",
                to="courses.course",
            ),
        ),
        migrations.AddField(
            model_name="courseenrollment",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                related_name="enrolled_courses",
                through="courses.CourseEnrollment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]