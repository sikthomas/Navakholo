from django.core.management.base import BaseCommand
from django.contrib.auth.management.commands.createsuperuser import Command as CreateSuperuserCommand
from django.core.management import CommandError
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

class Command(CreateSuperuserCommand):
    help = 'Create a superuser with idnumber.'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--idnumber', dest='idnumber', required=True,
            help='Specifies the idnumber for the superuser.',
        )

    def handle(self, *args, **options):
        idnumber = options.get('idnumber')
        if not idnumber:
            raise CommandError("You must provide the idnumber parameter.")
        
        # Ensure that the idnumber is valid and not already taken
        UserModel = get_user_model()
        if UserModel.objects.filter(idnumber=idnumber).exists():
            raise CommandError(f"An user with idnumber '{idnumber}' already exists.")
        
        # Set idnumber in options so it can be used in the super() call
        options['idnumber'] = idnumber

        # Create superuser
        super().handle(*args, **options)
        
        # Post-processing
        self.stdout.write(self.style.SUCCESS(f'Superuser created with idnumber: {idnumber}'))

    def get_input_data(self, *args, **kwargs):
        data = super().get_input_data(*args, **kwargs)
        data['idnumber'] = kwargs.get('idnumber')
        return data

    def prompt_user_input(self, field_name):
        if field_name == 'idnumber':
            while True:
                idnumber = input('ID Number: ')
                if idnumber:
                    return idnumber
                else:
                    self.stderr.write(_('Error: ID number is required.'))
