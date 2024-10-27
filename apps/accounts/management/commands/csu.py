from django.conf import settings
from django.core.management import BaseCommand

from apps.accounts.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.filter(email=settings.ADMIN_EMAIL).first()
        if user:
            self.stdout.write(self.style.WARNING('Администратор уже создан!'))
            return
        user = User.objects.create(
            email=settings.ADMIN_EMAIL,
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password(settings.ADMIN_PASSWORD)
        user.save()
        self.stdout.write(self.style.SUCCESS('Администратор был успешно создан!'))