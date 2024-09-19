import os
import shutil

import pytest

from user_sync.encryption import encrypt_file, decrypt_file
from user_sync.error import AssertionException



def test_encrypt_file(test_resources):
    private_key = test_resources['priv_key']
    encrypted_key = test_resources['priv_key_enc']
    passphrase = 'password'
    data = encrypt_file(passphrase, private_key)
    assert 'DEK-Info: DES-EDE3-CBC,' in data
    with pytest.raises(AssertionException):
        encrypt_file(passphrase, encrypted_key)
    with open(private_key, 'w') as f:
        f.write('invalid data')
    with pytest.raises(AssertionException):
        encrypt_file(passphrase, private_key)
    with open(private_key, 'w') as f:
        f.write('')
    with pytest.raises(AssertionException):
        encrypt_file(passphrase, private_key)


def test_decrypt_file(test_resources):
    private_key = test_resources['priv_key']
    encrypted_key = test_resources['priv_key_enc']
    passphrase = 'password'
    with open(private_key, 'r') as f:
        original = f.read()
    decrypted = decrypt_file(passphrase, encrypted_key)
    assert decrypted == original
    passphrase = 'wrong-password'
    with pytest.raises(AssertionException):
        decrypt_file(passphrase, encrypted_key)
    with open(encrypted_key, 'w') as f:
        f.write('invalid data')
    with pytest.raises(AssertionException):
        decrypt_file(passphrase, encrypted_key)


def test_encrypt_and_decrypt_file(test_resources):
    private_key = test_resources['priv_key']
    with open(private_key, 'r') as f:
        original = f.read()
    passphrase = 'password'
    encrypted = encrypt_file(passphrase, private_key)
    assert encrypted != original
    decrypted = decrypt_file(passphrase, private_key)
    assert decrypted == original
