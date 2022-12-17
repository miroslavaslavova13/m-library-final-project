from django.core import exceptions


def validate_only_letters(string):
    if not (any(ch.isalpha() for ch in string) and any(ch.isspace() for ch in string)):
        raise exceptions.ValidationError('Must contain only letters')
