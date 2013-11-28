#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      js201208030313
#
# Created:     28/11/2013
# Copyright:   (c) js201208030313 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def makeNdef(mb=1,me=0,cf=0,sr=1,il=0,tnf=0b000,_type="",payload="",uriIdentifier='00'):
    ndef=''
    type_hex=''
    payload_hex=''

    ndefInfo = mb<<7|me<<6|cf<<5|sr<<4|il<<3|tnf;
    ndefInfo_hex=hex(ndefInfo)[2:]
    if len(ndefInfo_hex)<2:
        ndefInfo_hex='0'+ndefInfo_hex

    typeLength = hex(len(_type))[2:]
    if len(typeLength)<2:
        typeLength='0'+typeLength

    for i in _type:
        tmp = i.encode('hex')
        if len(tmp)<2:
            tmp='0'+tmp
        type_hex +=tmp

    if _type=='U':
        payload_hex=uriIdentifier

    for i in payload:
        tmp = i.encode('hex')
        if len(tmp)<2:
            tmp='0'+tmp
        payload_hex +=tmp

    payloadLength = hex(len(payload_hex)/2)[2:]
    if len(payloadLength)<2:
        payloadLength='0'+payloadLength

    ndef = ndefInfo_hex+typeLength+payloadLength+type_hex+payload_hex

    return ndef

def main():
    print makeNdef(mb=1,me=0,tnf=0b001,\
        _type='U',payload="market://details?id=com.sec.smartview")
    print makeNdef(mb=0,me=1,tnf=0b100,\
        _type='android.com:pkg',payload='com.sec.smartview')

if __name__ == '__main__':
    main()
