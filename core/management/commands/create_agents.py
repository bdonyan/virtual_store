from django.core.management.base import BaseCommand
from core.models import Agent

class Command(BaseCommand):
    help = 'Create default agents'

    def handle(self, *args, **kwargs):
        agents = ['Tor', 'Mika', 'Kaa']
        for agent_name in agents:
            Agent.objects.get_or_create(name=agent_name)
        self.stdout.write(self.style.SUCCESS('Successfully created default agents'))
