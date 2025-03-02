print('Расшифрование файла')
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
code = 'nobodyknows'
with open('encrypted_data.bin','rb') as fobj:
    private_key = RSA.import_key(open('my_private_rsa_key.bin').read(),passphrase=code)
    enc_session_key, nonce, tag, cipertext = [fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]
    ciper_rsa = PKCS1_OAEP.new(private_key)
    session_key = ciper_rsa.decrypt(enc_session_key)
    ciper_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = ciper_aes.decrypt_and_verify(cipertext, tag)
print(data)