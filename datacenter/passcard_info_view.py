from django.shortcuts import render, get_object_or_404
from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': visit.format_duration(),
            'is_strange': visit.is_visit_long(),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)