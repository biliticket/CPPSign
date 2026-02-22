import hashlib

def get_sign(timestamp, nonce, ticketTypeId):
  return sign = hashlib.md5(
    f"cpp2C0T2y5u0m7a2d9l{timestamp}{nonce}{ticketTypeId}mKSEDLushKSIJSISHMNFEDNSUYQEAVJSfwp"[::-1].upper().encode('utf-8')
  ).hexdigest()

# 技术本无罪，就看谁先捅破那层窗户纸
# 技术共享早就不可能成立了
# 各位，祝好
