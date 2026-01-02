from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')


        # Create Users
        users = [
            User(name='Tony Stark', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Steve Rogers', email='captain@marvel.com', team=marvel, is_superhero=True),
            User(name='Bruce Wayne', email='batman@dc.com', team=dc, is_superhero=True),
            User(name='Clark Kent', email='superman@dc.com', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=date(2026, 1, 1))
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=date(2026, 1, 2))
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=date(2026, 1, 3))
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=date(2026, 1, 4))

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create Workouts
        Workout.objects.create(name='Push Ups', description='Upper body workout', suggested_for='Marvel')
        Workout.objects.create(name='Sit Ups', description='Core workout', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
