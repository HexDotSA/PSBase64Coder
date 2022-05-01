import sys
from base64 import b64encode,b64decode

if len(sys.argv) < 2:
    print ("Usage: python3 ps-decode.py <Decode or Encode> <(Encoded || Decoded) Command>")
    sys.exit(-1)

funcType = sys.argv[1]
Command = str(sys.argv[2])

if funcType.lower().strip() == "decode":
  try:
      print (b64decode(Command).decode('UTF-16LE'))
  except Exception as e:
      print (str(e))

elif funcType.lower().strip() == "encode":
  try:
      print ("Powershell.exe -enc " + b64encode(Command.strip().encode('UTF-16LE')))
  except Exception as e:
      print (str(e))
