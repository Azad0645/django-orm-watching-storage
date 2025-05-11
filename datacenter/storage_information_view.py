from django.shortcuts import render
from datacenter.models import Visit


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in active_visits:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': visit.format_duration(),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)