from hypothesis import given, strategies as st, settings, Verbosity
import yaml

YAML_ALPHABET = list(
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "-_:{}[](),&*!?|>'\"%#@/\\"
    " \n\t"
)

YAML_EXAMPLES = 1000000

ALLOWED_YAML_EXCEPTIONS = (
    yaml.YAMLError,
    UnicodeError,
    ValueError,
    OverflowError,
)


@given(st.text(alphabet=YAML_ALPHABET, min_size=0, max_size=100000))
@settings(
    verbosity=Verbosity.verbose,
    max_examples=YAML_EXAMPLES,
    deadline=None,
)
def test_yaml_safe_load(input_string):
    try:
        yaml.safe_load(input_string)
    except ALLOWED_YAML_EXCEPTIONS:
        return


@given(st.text(alphabet=YAML_ALPHABET, min_size=0, max_size=300))
@settings(
    verbosity=Verbosity.verbose,
    max_examples=YAML_EXAMPLES,
    deadline=None,
)
def test_yaml_scan(input_string):
    try:
        list(yaml.scan(input_string))
    except ALLOWED_YAML_EXCEPTIONS:
        return


@given(st.text(alphabet=YAML_ALPHABET, min_size=0, max_size=300))
@settings(
    verbosity=Verbosity.verbose,
    max_examples=YAML_EXAMPLES,
    deadline=None,
)
def test_yaml_compose(input_string):
    try:
        yaml.compose(input_string)
    except ALLOWED_YAML_EXCEPTIONS:
        return


if __name__ == "__main__":
    test_yaml_safe_load()
    test_yaml_scan()
    test_yaml_compose()
