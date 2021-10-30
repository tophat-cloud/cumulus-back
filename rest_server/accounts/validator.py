from django.forms import ValidationError
from django.utils.translation import gettext as _


class AlphabetPasswordValidator:
    """
    Validate whether the password is alphanumeric.
    """
    def validate(self, password, user=None):
        if password.isalpha():
            raise ValidationError(
                _("This password is entirely alphabet."),
                code='password_entirely_alphabet',
            )

    def get_help_text(self):
        return _('Your password can’t be entirely alphabet.')