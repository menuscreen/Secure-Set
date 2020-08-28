#!/usr/bin/python3
import hmac
import hashlib

#use this script in the same directory as the .key and .txt file
#script is used to validate the hash digests of messages in the tags.txt using master.key

#created a variable to reference the master.key file
masterkey = open("master.key", 'r')

#created a dictionary out of the tag.txt file
dictionary = {}
with open("tags.txt") as f:
    #for loop to remove line breaks and split at the colon of each line
    for line in f:
        #the message will become the key and the hash will be the value
        (key, val) = line.rstrip('\n').split(':')
        dictionary[key] = val
    #commented out print statement for use during testing
    #print(dictionary)

#set variable to call the keys/messages from the txt file
msg = dictionary.keys()
#set a variable to read the master.key file as a string
key = masterkey.read()

#created a list to store the calculated hash values using the masterkey
l = []
#for loop reads through each element in msg list to compute hashes
for m in msg:
    hm = hmac.new(key.encode(),m.encode(),hashlib.md5)
    #stores the msg and calculated hashes in list l joined by :
    l.append(m + ':' + hm.hexdigest())
#print statements commented out for use during testing
#print(l)
#print('\n')

#created a dictionary from list l
checklist = {}
for i in l:
    (key, val) = i.rstrip('\n').split(':')
    checklist[key] = val
#commented out print statement for use from testing
#print(checklist)

#created two lists to store true and false messages
truemsg = []
falsemsg = []
#created a for loop to check if master key msg hash matches original msg hash
for x in checklist.values():
    if x in dictionary.values():
        #commented out print statement for use during testing
        #print(x + " | Message verified as true.")
        #if the masterkey hash matches original message hash, add to true list
        truemsg.append(x)
    else:
        #commented out print statement for use during testing
        #print(x + " | WARNING! Message NOT verified.")
        #if masterkey hash does not match original msg hash, add to false list
        falsemsg.append(x)
#commented out print statements for use during testing
#print(truemsg)
#print(falsemsg)

#created a reverse dictionary from masterhash checklist
#reverse dict used to call the original message rather than the hashed value
#as long as keys and values are unique, okay to swap
reverse_checklist = {value : key for (key, value) in checklist.items()}
#commented out print statement used during testing
#print(reverse_checklist)

#print("Check Complete: The following messages have been verified: ")
#commented out message displaying true results, since only want false results
#for m in truemsg:
#    print('    ' + reverse_checklist[m] + ':' + m)

print("WARNING! These messages could not be verified!: ")
#loops through false msg list, and prints each item and hash not verified
for m in falsemsg:
    #could place an if check here if there were no false msgs
    print('    ' + reverse_checklist[m] + ':' + m)

#close the masterkey file
masterkey.close()

