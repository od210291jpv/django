# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

# Student model


class Student(models.Model):

    class Meta(object):
        verbose_name = u"Student"
        verbose_name_plural = u"Students"


    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'first_name'
    )
    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'last_name'
    )
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u'middle_name',
        default=' '
    )
    birthdate = models.DateField(
        blank=False,
        verbose_name=u'birth_date',
        null=True
    )
    photo = models.ImageField(
        blank=True,
        verbose_name=u'avatar',
        null=True
    )
    ticket = models.IntegerField(
        blank=False,
        verbose_name=u'ticket'
    )
    notes = models.TextField(
        blank=True,
        verbose_name=u'notes'
    )

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):

    class Meta(object):
        verbose_name = u'Group'
        verbose_name_plural = u'Groups'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Group title'
    )

    leader = models.OneToOneField('Student',
        null=True,
        blank=True,
        verbose_name=u'Group leader',
        on_delete=models.SET_NULL
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u'Additional notes'
    )

    def __unicode__(self):
        if self.leader:
            return u'%s (%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u'%s' % (self.title)