from unittest import TestCase

from django.core.exceptions import ValidationError

from m_library.core.validators import validate_only_letters


class ValidatorOnlyLettersTests(TestCase):

    def test_validate_only_letters_validator_with_only_letters_expect_ok(self):
        validate_only_letters('UsedOnlyletters')

    def test_validate_only_letters_validator_with_numbers_expect_raise_exception(self):
        with self.assertRaises(ValidationError) as error:
            validate_only_letters('usedlettersaandnumbers123')

        self.assertIsNotNone(error.exception)
        self.assertEqual('Must contain only letters', error.exception.message)

    def test_validate_only_letters_validator_with_spaces_expect_raise_exception(self):
        with self.assertRaises(ValidationError) as error:
            validate_only_letters('  ')

        self.assertIsNotNone(error.exception)
        self.assertEqual('Must contain only letters', error.exception.message)

    def test_validate_only_letters_validator_with_empty_string_expect_raise_exception(self):
        with self.assertRaises(ValidationError) as error:
            validate_only_letters('')

        self.assertIsNotNone(error.exception)
        self.assertEqual('Must contain only letters', error.exception.message)

    def test_validate_only_letters_validator_with_spaces_and_numbers_expect_raise_exception(self):
        with self.assertRaises(ValidationError) as error:
            validate_only_letters('  123')

        self.assertIsNotNone(error.exception)
        self.assertEqual('Must contain only letters', error.exception.message)

    def test_validate_only_letters_validator_with_letters_numbers_and_spaces_expect_raise_exception(self):
        with self.assertRaises(ValidationError) as error:
            validate_only_letters('Test 123')

        self.assertIsNotNone(error.exception)
        self.assertEqual('Must contain only letters', error.exception.message)
