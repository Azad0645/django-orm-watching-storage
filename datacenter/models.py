from django.db import models
from django.utils import timezone
from datetime import timedelta

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if self.leaved_at:
            return self.leaved_at - self.entered_at
        return timezone.now() - self.entered_at

    def is_visit_long(self, minutes=60):
        return self.get_duration() > timedelta(minutes=minutes)

    def format_duration(self):
        delta = self.get_duration()
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // SECONDS_IN_HOUR
        minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
        seconds = total_seconds % SECONDS_IN_MINUTE
        return f"{hours}:{minutes:02d}:{seconds:02d}"