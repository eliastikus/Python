import pyAesCrypt

password = input('Entry your password: ')


pyAesCrypt.encryptFile('Code', 'code.aes', password)

pyAesCrypt.decryptFile('Code.aes', 'codeout', password)
