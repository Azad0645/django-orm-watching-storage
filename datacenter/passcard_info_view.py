from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime, now
from datacenter.models import Passcard, Visit


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        entered_at = localtime(visit.entered_at)
        if visit.leaved_at:
            duration = visit.leaved_at - visit.entered_at
        else:
            duration = now() - visit.entered_at

        visit_info = {
            'entered_at': entered_at.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': format_duration(duration),
            'is_strange': duration.total_seconds() > 3600
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)