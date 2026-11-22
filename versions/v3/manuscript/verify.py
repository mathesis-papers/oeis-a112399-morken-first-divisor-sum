import argparse
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path


def mobius_trial(value):
    remaining = value
    sign = 1
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            remaining //= candidate
            sign = -sign
            if remaining % candidate == 0:
                return 0
        candidate += 1
    return -sign if remaining > 1 else sign


def mobius_sieve(bound):
    values = [1] * (bound + 1)
    values[0] = 0
    primes = bytearray(b'\x01') * (bound + 1)
    primes[0:2] = b'\x00\x00'
    for prime in range(2, bound + 1):
        if primes[prime]:
            for multiple in range(prime, bound + 1, prime):
                values[multiple] = -values[multiple]
                if multiple > prime:
                    primes[multiple] = 0
            square = prime * prime
            for multiple in range(square, bound + 1, square):
                values[multiple] = 0
    return values


def divisors(value):
    result = []
    for candidate in range(1, isqrt(value) + 1):
        if value % candidate == 0:
            result.append(candidate)
            other = value // candidate
            if other != candidate:
                result.append(other)
    return sorted(result)


def radical(value):
    product = 1
    remaining = value
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            product *= candidate
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    return product * remaining


def totient(value):
    return sum(gcd(index, value) == 1 for index in range(1, value + 1))


def powerful(value):
    remaining = value
    candidate = 2
    while candidate * candidate <= remaining:
        exponent = 0
        while remaining % candidate == 0:
            remaining //= candidate
            exponent += 1
        if exponent == 1:
            return 0
        candidate += 1
    return int(remaining == 1)


def require_equal(actual, expected, statement, parameters):
    if actual != expected:
        raise ValueError(f'{statement}: {parameters}: {actual} != {expected}')


def verify():
    bound = 160000
    values = mobius_sieve(bound)
    for value in range(1, bound + 1):
        require_equal(values[value], mobius_trial(value), 'Mobius implementations', value)
    mertens = [0]
    for value in values[1:]:
        mertens.append(mertens[-1] + value)

    def coprime(parameter, cutoff):
        return sum(values[index] for index in range(1, cutoff + 1) if gcd(index, parameter) == 1)

    def first(parameter, cutoff):
        return sum(coprime(divisor, cutoff // divisor) for divisor in divisors(parameter) if values[divisor])

    def second(parameter, cutoff):
        return sum(mertens[cutoff // index] for index in range(1, cutoff + 1) if parameter % radical(index) == 0)

    sequence = [0] + [coprime(parameter, parameter) for parameter in range(1, 401)]
    transform = [0] + [sum(values[index // gcd(index, parameter)] for index in range(1, parameter + 1)) for parameter in range(1, 401)]
    for parameter in range(1, 401):
        expected = sequence[parameter]
        require_equal(first(parameter, parameter), expected, 'First conjecture', parameter)
        require_equal(second(parameter, parameter), expected, 'Second conjecture', parameter)
        require_equal(sum(values[parameter * index] for index in range(1, parameter + 1)), values[parameter] * expected, 'Product identity', parameter)
        require_equal(transform[parameter], sum(sequence[divisor] for divisor in divisors(parameter)), 'Inverse Mobius transform', parameter)
        require_equal(expected, sum(values[parameter // divisor] * transform[divisor] for divisor in divisors(parameter)), 'Mobius transform', parameter)
    for parameter in range(1, 61):
        for cutoff in range(121):
            expected = coprime(parameter, cutoff)
            require_equal(first(parameter, cutoff), expected, 'First cutoff identity', [parameter, cutoff])
            require_equal(second(parameter, cutoff), expected, 'Second cutoff identity', [parameter, cutoff])
            require_equal(sum(values[parameter * index] for index in range(1, cutoff + 1)), values[parameter] * expected, 'Product cutoff identity', [parameter, cutoff])
    previous = 0
    for cutoff in range(1, 121):
        direct = sum(values[row * column] for row in range(1, cutoff + 1) for column in range(1, cutoff + 1))
        quadratic = sum(values[divisor] * coprime(divisor, cutoff // divisor) ** 2 for divisor in range(1, cutoff + 1))
        require_equal(quadratic, direct, 'Quadratic identity', cutoff)
        require_equal(-1 + 2 * sum(values[index] * sequence[index] for index in range(1, cutoff + 1)), direct, 'Row identity', cutoff)
        if values[cutoff] == 0:
            require_equal(direct, previous, 'Nonsquarefree plateau', cutoff)
        previous = direct
    reference_prefix = [1, 1, 0, 0, -1, 0, -1, -2, -2, -1, -1, -2, -2, -3, -2, -3, -1, -4, -2, -5]
    require_equal(sequence[1:21], reference_prefix, 'A112399 prefix', [1, 20])
    for horizontal in range(41):
        for vertical in range(41):
            direct = sum(values[row * column] for row in range(1, horizontal + 1) for column in range(1, vertical + 1))
            rectangular = sum(values[divisor] * coprime(divisor, horizontal // divisor) * coprime(divisor, vertical // divisor) for divisor in range(1, min(horizontal, vertical) + 1))
            require_equal(rectangular, direct, 'Rectangular identity', [horizontal, vertical])

    counts = [0] + [sum(values[index] ** 2 for index in range(1, parameter + 1) if gcd(index, parameter) == 1) for parameter in range(1, 201)]
    transforms = [0] + [sum(counts[divisor] for divisor in divisors(parameter)) for parameter in range(1, 201)]
    phi = [0] + [totient(parameter) for parameter in range(1, 201)]
    gcd_mu = [0]
    prime_power_cases = 0
    for parameter in range(1, 201):
        inclusive = sum(values[index // gcd(index, parameter)] ** 2 for index in range(1, parameter + 1))
        lcm_version = sum(values[(parameter * index // gcd(index, parameter)) // parameter] ** 2 for index in range(1, parameter + 1))
        strict = sum(sum(values[index] ** 2 for index in range(1, divisor) if gcd(index, divisor) == 1) for divisor in divisors(parameter))
        require_equal(transforms[parameter], inclusive, 'Squarefree count transform', parameter)
        require_equal(lcm_version, inclusive, 'Squarefree lcm transform', parameter)
        require_equal(strict, inclusive - 1, 'Strict endpoint correction', parameter)
        require_equal(counts[parameter], sum(values[parameter // divisor] * transforms[divisor] for divisor in divisors(parameter)), 'Squarefree inverse transform', parameter)
        if inclusive > parameter:
            raise ValueError('Squarefree transform bound')
        first_gcd = sum(values[gcd(index, parameter)] for index in range(1, parameter + 1))
        gcd_mu.append(first_gcd)
        require_equal(first_gcd, sum(values[divisor] * phi[parameter // divisor] for divisor in divisors(parameter)), 'A007431 convolution', parameter)
        square_gcd = sum(values[gcd(index, parameter)] ** 2 for index in range(1, parameter + 1))
        require_equal(square_gcd, sum(values[divisor] ** 2 * phi[parameter // divisor] for divisor in divisors(parameter)), 'A063659 convolution', parameter)
        quotient_gcd = sum(values[parameter // gcd(index, parameter)] for index in range(1, parameter + 1))
        prime_divisors = [prime for prime in divisors(parameter) if prime > 1 and len(divisors(prime)) == 2]
        product = 1
        for prime in prime_divisors:
            product *= 2 - prime
        require_equal(quotient_gcd, product, 'A276833 product', parameter)
        require_equal(quotient_gcd, sum(values[divisor] * phi[divisor] for divisor in divisors(parameter)), 'A276833 divisor formula', parameter)
        require_equal(quotient_gcd, sum(values[(parameter * index // gcd(index, parameter)) // index] for index in range(1, parameter + 1)), 'A276833 lcm formula', parameter)
        require_equal(powerful(parameter) * values[parameter], int(parameter == 1), 'Powerful signed correction', parameter)
        expected_variant = 1
        for prime in prime_divisors:
            exponent = 0
            remaining = parameter
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            expected_variant *= 0 if exponent == 1 else -1
        require_equal(powerful(parameter) * values[radical(parameter)], expected_variant, 'Powerful corrected variant', parameter)
        if len(prime_divisors) == 1:
            prime = prime_divisors[0]
            exponent = 0
            remaining = parameter
            while remaining > 1:
                remaining //= prime
                exponent += 1
            parity = exponent % 2
            expected = 1 + sum(sum(values[index] ** 2 for index in range(1, prime ** power)) for power in range(parity, exponent + 1, 2))
            require_equal(inclusive, expected, 'A304575 prime power', [prime, exponent])
            require_equal(first_gcd, prime - 2 if exponent == 1 else prime ** (exponent - 2) * (prime - 1) ** 2, 'A007431 prime power', [prime, exponent])
            require_equal(square_gcd, prime if exponent == 1 else prime ** exponent - prime ** (exponent - 2), 'A063659 prime power', [prime, exponent])
            prime_power_cases += 1
    require_equal(transforms[1], 1, 'A304575 exponent zero', 1)
    for parameter in range(1, 201):
        require_equal(sum(gcd_mu[divisor] for divisor in divisors(parameter)), phi[parameter], 'A007431 divisor transform', parameter)
    for parameter in range(1, 51):
        for cutoff in range(71):
            for function in [lambda index: values[index], lambda index: values[index] ** 2, lambda index: index ** 2 + (-1) ** index]:
                direct = sum(function(index // gcd(index, parameter)) for index in range(1, cutoff + 1))
                grouped = sum(sum(function(index) for index in range(1, cutoff * divisor // parameter + 1) if gcd(index, divisor) == 1) for divisor in divisors(parameter))
                require_equal(direct, grouped, 'General arbitrary-cutoff grouping', [parameter, cutoff])
    for cutoff in range(1, 161):
        row = [coprime(divisor, cutoff // divisor) for divisor in range(1, cutoff + 1)]
        for divisor, entry in enumerate(row, 1):
            require_equal(entry, second(divisor, cutoff // divisor), 'A400203 supported Mertens formula', [cutoff, divisor])
            if divisor == 1:
                require_equal(entry, mertens[cutoff], 'A400203 first column', cutoff)
            if 2 * divisor > cutoff:
                require_equal(entry, 1, 'A400203 upper boundary', [cutoff, divisor])
            require_equal(entry, coprime(divisor, (divisor * (cutoff // divisor)) // divisor), 'A400203 plateau', [cutoff, divisor])
            if divisor < cutoff:
                increment = values[cutoff // divisor] if cutoff % divisor == 0 and gcd(cutoff // divisor, divisor) == 1 else 0
                require_equal(entry - coprime(divisor, (cutoff - 1) // divisor), increment, 'A400203 increment', [cutoff, divisor])
        require_equal(sum(row), sum(powerful(index) for index in range(1, cutoff + 1)), 'A400203 powerful row', cutoff)
        require_equal(sum(values[index] * row[index - 1] for index in range(1, cutoff + 1)), sum(values[index] * len(divisors(index)) for index in range(1, cutoff + 1)), 'A400203 Mobius row', cutoff)
        require_equal(sum(values[index] ** 2 * row[index - 1] for index in range(1, cutoff + 1)), 1, 'A400203 squarefree row', cutoff)
    return {
        'status': 'pass',
        'arithmetic': 'exact integers',
        'mobius_implementations': {'trial_factorization_vs_sieve': [1, bound]},
        'a112399_first_and_second': {'n': [1, 400]},
        'a332685_transforms': {'n': [1, 400]},
        'a372706_product': {'n': [1, 400]},
        'arbitrary_cutoff_first_second_product': {'n': [1, 60], 'X': [0, 120], 'pairs': 7260},
        'a372700_quadratic_row_and_plateau': {'N': [1, 120]},
        'a112399_reference_prefix': {'n': [1, 20], 'values': reference_prefix},
        'rectangular_identity': {'X': [0, 40], 'Y': [0, 40], 'pairs': 1681},
        'finite_gcd_and_squarefree_transforms': {'n': [1, 200]},
        'prime_power_formulas': {'prime_powers_at_most': 200, 'positive_exponent_cases': prime_power_cases, 'exponent_zero': 'pass'},
        'general_cutoff_grouping': {'n': [1, 50], 'X': [0, 70], 'functions': ['mu', 'mu^2', 'm^2+(-1)^m'], 'comparisons': 10650},
        'a400203_all_finite_formulas': {'N': [1, 160], 'triangle_entries': 12880},
        'corrections': {'a304575_strict_endpoint': {'n': [1, 200], 'inclusive_minus_strict': 1}, 'a112526_signed_variant': {'n': [1, 200]}},
        'scope': 'Finite checks; all-input statements have written proofs in note.tex.',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description='Check the Mobius sum identities by direct integer arithmetic.')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(verify(), indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
