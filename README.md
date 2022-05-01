# PSBase64Coder
> This is a python script to encode payload as UTF-16LE which is the type of base64 encoding that powershell understand. <br /> 
> There are two functions, one for encoding and the other is for decoding.

## Exmaple: 
`└─$ python psEncode.py encode "curl http://TEST.T/index.html"`
<br /> Output: <br />
` Powershell.exe -enc YwB1AHIAbAAgAGgAdAB0AHAAOgAvAC8AVABFAFMAVAAuAFQALwBpAG4AZABlAHgALgBoAHQAbQBsAA==   `
