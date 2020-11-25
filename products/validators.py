from django.core.exceptions import ValidationError
import re


def validate_box_size(value):
    """
    Validate Box Size
    :param value: String Values
    :return: ValidationError or None
    """
    patterns = [r"\d+x\d+x\d+", r"\d+х\d+х\d+"]
    for pattern in patterns:
        find = re.search(pattern, value)
        if find:
            break
        elif not find:
            raise ValidationError(
                '%(value)s is not match the format "DDxDDxDD"',
                params={'value': value})


def validate_article_number(value):
    """
    Validate Article Number, should contain only digits
    :param value: Article Number Value
    :return: ValidationError or None
    """
    if not value.replace('.', '').isdigit():
        raise ValidationError('%(value)s should contain only digits', params={'value': value})
