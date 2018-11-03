from flapp.validation.validator import Validator
from flapp.validation import rules

register_dto_validator = Validator(
    rules.field('username',
        rules.required(),
        rules.min_length(3),
        rules.max_length(20)
    ),
    rules.field('password',
        rules.required(),
        rules.min_length(3),
        rules.max_length(20)
    )
)
