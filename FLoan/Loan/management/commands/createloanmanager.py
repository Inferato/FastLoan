from django.core.management.base import BaseCommand
from ...user import User


class Command(BaseCommand):
    help = u'Create a user with "Loan Manager" role'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('email', type=str, help='E-mail')
        parser.add_argument('pwd', type=str, help='Password')
        parser.add_argument('-fn', '--first_name', type=str, help='First name(optional)')
        parser.add_argument('-ln', '--last_name', type=str, help='Last name (optional)')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        pwd = options['pwd']
        first_name = options['first_name']
        last_name = options['last_name']
        User.objects.create_user(username=username, email=email, password=pwd, IsLoanOfficer=True)
