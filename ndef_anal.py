#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      js201208030313
#
# Created:     06/11/2013
# Copyright:   (c) js201208030313 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
ndef_raw="D101225402656E546869732069732073616D706C65207465787420666F722074657374696E67"
ndef=ndef_raw.decode('hex')
tnfDict={0x00:'Empty',0x01:'NFC Forum well-known type',\
         0x02:'MIME',0x03:'Absolute URI',0x04:'NFC Forum external type',\
         0x05:'UnKnown',0x06:'Unchange',0x07:'Reserved'}
def main():
    message_size=len(ndef)
    record=ndef[0:]
    temp =int(record[0].encode('hex'),16)
    mb_flag = (temp&0x80)>>7
    me_flag = (temp&0x40)>>6
    cf_flag = (temp&0x20)>>5
    sr_flag = (temp&0x10)>>4
    il_flag = (temp&0x08)>>3
    tnf = temp&0b111
    print "Header 1st : "+hex(temp)
    print "MB : ",mb_flag,"ME : ",me_flag,"CF : ",cf_flag,"SR : ",sr_flag,"IL : ",il_flag,"TNF : ",tnf,tnfDict[tnf]

    typeLength = int(record[1].encode('hex'),16)
    print "Type length is ", typeLength
    if sr_flag == 1:#shor record
        payload_length = int(record[2].encode('hex'),16)
        print "Payload length is ",payload_length
    else:
        print " You have to write code for normal record"

    if il_flag ==0:
        typeField = record[3:3+typeLength]
        print "typefield : ",typeField
        payloadField = record[3+typeLength:3+typeLength+payload_length]

        print payloadField

        recordLen=3+typeLength+payload_length
        if recordLen == message_size:
            stopAnal = True
        else:
            stopAnal = False
    else:
        print " You have to write code for ID present state"

    if stopAnal==False:
        print "You have to add for next record"

if __name__ == '__main__':
    main()
