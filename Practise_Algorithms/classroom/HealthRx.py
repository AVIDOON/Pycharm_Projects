import base64 as b64

decodedString = open("/Users/avinashraj/Desktop/Backend_TestEvaluation/Encoded File.b64", "r").read()
with open('HealthRxFin.pdf', 'wb') as currentModule:
  currentModule.write(b64.b64decode(decodedString))

