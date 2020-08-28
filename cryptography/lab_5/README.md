# Lab 5: Authenticating message hash digests
Hash-based Message Authentication Codes can be used to validate the
integrity of an encrypted method. In the Python package, hmac, you can use
the hmac.new() command and the hmac.update() to calculate the hash.

In this lab, the goal is to read through the tags.txt file and validate the hash digest of each message. 
If the hash doesn't match, the python script will output the massages that cannot be trusted.
