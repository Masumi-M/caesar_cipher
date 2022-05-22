# -*- coding: utf-8 -*-

import string


def caesar_parser(
    target_str: string,
    shift_key: int,
    is_encode: bool,
    verbose: bool = False,
) -> string:
    """Parser for caesar cipher

    Args:
        target_str (string): string data that you want to parse.
        shift_key (int): number of char to shift.
        is_encode (bool): true for encode and false for decode.
        verbose (bool, optional): verbose flag. Defaults to False.

    Returns:
        string: encoded or decoded string data
    """
    temp_enc = ""
    sign = 1 if is_encode else -1
    for char in list(target_str):
        target_str_ascii = ord(char)
        shift_key = shift_key % 26
        if 65 <= target_str_ascii and target_str_ascii <= 90:  # A~Z
            target_str_ascii = target_str_ascii + shift_key * sign
            if target_str_ascii > 90:
                target_str_ascii = target_str_ascii - 26
            elif target_str_ascii < 65:
                target_str_ascii = target_str_ascii + 26
        elif 97 <= target_str_ascii & target_str_ascii <= 122:  # a~z
            target_str_ascii = target_str_ascii + shift_key * sign
            if target_str_ascii > 122:
                target_str_ascii = target_str_ascii - 26
            elif target_str_ascii < 97:
                target_str_ascii = target_str_ascii + 26
        else:  # symbolic-char
            pass
        temp_enc += chr(target_str_ascii)
    if verbose: print(f"{target_str} => {temp_enc} (shift_key: {shift_key})")
    return temp_enc


def caesar_encode(
    target_str: string,
    shift_key: int,
    verbose: bool = False,
) -> string:
    """Encoder for caesar cipher

    Args:
        target_str (string): plain text that you want to parse.
        shift_key (int): number of char to shift.
        verbose (bool, optional): verbose flag. Defaults to False.

    Returns:
        string: encoded string data (cipher text)
    """
    return caesar_parser(
        target_str,
        shift_key,
        is_encode=True,
        verbose=verbose,
    )


def caesar_decode(
    target_str: string,
    shift_key: int,
    verbose: bool = False,
) -> string:
    """Decoder for caesar cipher

    Args:
        target_str (string): cipher text that you want to parse.
        shift_key (int): number of char to shift.
        verbose (bool, optional): verbose flag. Defaults to False.

    Returns:
        string: decoded string data (plain text)
    """
    return caesar_parser(
        target_str,
        shift_key,
        is_encode=False,
        verbose=verbose,
    )
