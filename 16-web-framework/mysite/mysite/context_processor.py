from users.models import Timesheet


def is_ready_to_work(request):
    if request.user.is_authenticated:
        if Timesheet.objects.filter(user_id=request.user.id, end_date=None).exists():
            return {'ready_to_work': False}
        return {'ready_to_work': True}
    return {}
