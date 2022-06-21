from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from articles.models.common import Member


class Student(Member):
    viewedGuides = models.ManyToManyField(
        verbose_name=_("video guides"),
        to="Guide",
        through="LearningProgress",
        blank=True,
        related_name="studentViews",
        related_query_name="studentView",
        help_text=_("all guides viewed by this student."),
    )
    savedGuides = models.ManyToManyField(
        verbose_name=_("saved guides"),
        to="Guide",
        blank=True,
        related_name="studentSaved",
        related_query_name="studentSaved",
        help_text=_("all guides saved by this student."),
    )

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")
        default_permissions = []

    def __str__(self):
        return self.fullName

    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.pk)])


class LearningProgress(models.Model):
    student = models.ForeignKey(
        verbose_name=_("student"), to=Student, on_delete=models.CASCADE
    )
    guide = models.ForeignKey(
        verbose_name=_("guide"), to="Guide", on_delete=models.SET_NULL, null=True
    )
    startDate = models.DateTimeField(verbose_name=_("start date"), null=True)
    lessonsCompleted = models.PositiveSmallIntegerField(
        verbose_name=_("lessons completed"),
    )
    completionDate = models.DateTimeField(verbose_name=_("completion date"), null=True)

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")
        unique_together = ["student", "guide"]
        default_permissions = []

    def __str__(self):
        return "%(student)s's learning progress" % {"student": self.student.fullName}

    def get_absolute_url(self):
        return reverse("learning-progress-detail", kwargs={"pk": str(self.pk), "version": "v1"})
