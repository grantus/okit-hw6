from hypothesis import given, strategies as st, settings, Verbosity, example
from calc import calculate, opn, CalcException
# from correct_calc import calculate, opn, CalcException

ALPHABET = list("0123+-*/%^!(). ")


# Генерируем более общие арифметические выражения
@given(st.text(alphabet=ALPHABET, min_size=0, max_size=25))
@example("0^(0-1)")
@settings(verbosity=Verbosity.verbose, max_examples=100000, derandomize=True, deadline=None)  # Включает подробный вывод
def test_calculate_with_processed_input(input_string):
    processed_input = ""
    try:
        # Сначала преобразуем входное выражение в ОПН
        processed_input = opn(input_string)
    except Exception as e:
        # Ошибки, связанные с обработкой выражения, могут быть проигнорированы
        pass
    try:
        calculate(processed_input)
    except (CalcException, OverflowError, ValueError):
        return
    # CalcException, OverflowError и ValueError можно игнорировать и заглушать


if __name__ == "__main__":
    test_calculate_with_processed_input()
