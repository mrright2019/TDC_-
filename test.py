
import execjs
ctx = execjs.compile(open("tdc.js","r").read())
eks,gdata = ctx.call("add_x")
print(eks)
print(gdata)
eks,gdata = ctx.call("add_x")
print(eks)
print(gdata)

