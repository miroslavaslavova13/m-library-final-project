from django.core import exceptions


def validate_only_letters(string):
    if (not (all(chr.isalpha() or chr.isspace() for chr in string))) or string.strip() == "":
        raise exceptions.ValidationError('Must contain only letters')
