from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

# ignore warnings
from django.template.loader import render_to_string
from gpu.models import GPUModel, HistoricalPrice, Notification


def craft_html(notifications):
    return render_to_string('../templates/client/notification.html', {'notifications': notifications})


class Command(BaseCommand):
    help = 'Update out.csv with scraped data'

    def handle(self, *args, **options):
        for user in User.objects.all():
            all_notifications = Notification.objects.all().filter(user=user)
            new_notifications = []
            for notif in all_notifications:
                if notif.gpu.get_hist_prices()[0].decreased:
                    new_notifications.append(notif)
            if new_notifications:
                send_mail(
                    subject='Subject here',
                    message='Here is the message.',
                    html_message=craft_html(new_notifications),
                    from_email=None,  # uses default email in CheapPC.settings
                    recipient_list=[user.email],
                    fail_silently=False,
                )
