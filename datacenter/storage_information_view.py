from django.utils.timezone import localtime, now
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in active_visits:
        entered_at = localtime(visit.entered_at)
        duration = now() - visit.entered_at
        duration_str = format_duration(duration)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_at.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': duration_str,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)