import requests
import re,time

from det import *




cookie_str = "TDC_itoken=1117279312%3A1587446300"
cookies = {
  "TDC_itoken":'1117279312%3A1587446300'
}

sess = requests.Session()

createIframeStart = str(int(time.time()*1000))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Referer': 'https://007.qq.com/online.html',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

ptcz = '64c6eaeb4bd663d6117a7d5fce3ed215e87dadf70aed38aeeca90ef8139c9924'

params = (
    ('aid', '2100049390'),
    ('protocol', 'https'),
    ('accver', '1'),
    ('showtype', 'popup'),
    ('ua', 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NzUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83NS4w'),
    ('noheader', '1'),
    ('fb', '1'),
    ('enableDarkMode', '0'),
    ('fpinfo', 'fpsig=undefined'),
    ('grayscale', '1'),
    ('clientype', '2'),
    ('cap_cd', ''),
    ('uid', '2819700269'),
    ('wxLang', ''),
    ('subsid', '1'),
    ('callback', '_aq_64821'),
    ('sess', ''),
)

response = sess.get('https://ssl.captcha.qq.com/cap_union_prehandle', headers=headers, params=params)

import json,time

data = json.loads(response.content.decode("utf-8").replace("_aq_64821(","")[:-1])
print(data)

sess_ = data['sess']
sid = data['sid']




params = (
    ('0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'),
    ('1', 'zh-CN'),
    ('2', '1.8'),
    ('3', '1.8'),
    ('4', '24'),
    ('5', '6'),
    ('6', '-480'),
    ('7', '1'),
    ('8', '1'),
    ('9', '1'),
    ('10', 'u'),
    ('11', 'undefined'),
    ('12', 'u'),
    ('13', 'Win32'),
    ('14', 'unspecified'),
    ('15', 'e466827d3971a555235e032f6e6f19d2'),
    ('16', 'a7bc50d4cdc0a49bdd948adde466aeb5'),
    ('17', 'e3cf09cd89763e62623a65a77c741594'),
    ('18', '0'),
    ('19', '83f619edd084ef69de541dd8973c2320'),
    ('20', '10401920241080192024'),
    ('21', '1;'),
    ('22', '1;1;1;1;1;1;1;0;1;object0UTF-8'),
    ('23', '0'),
    ('24', '0;0'),
    ('25', '39efe514b8b0ae9b048fe4d2074540a9'),
    ('26', '44100_0_1_0_2_explicit_speakers'),
    ('27', 'c8205b36aba2b1f3b581d8170984e918'),
    ('28', 'ANGLE(Intel(R)UHDGraphics630Direct3D11vs_5_0ps_5_0)'),
    ('29', '2a4bdde0b1902c187a151c77e5b69d33'),
    ('30', '267301cb561d8b8f1b6749e8d046e11e'),
    ('31', '0'),
    ('32', '0'),
    ('33', '0'),
    ('34', '0'),
    ('35', '0'),
    ('36', '0'),
    ('37', '0'),
    ('38', '0'),
    ('39', '0'),
    ('40', '0'),
    ('41', '0'),
    ('42', '0'),
    ('43', '0'),
    ('44', '0'),
    ('45', '0'),
    ('46', '0'),
    ('47', '0'),
    ('48', '0'),
    ('49', '0'),
    ('50', '0'),
    ('fesig', '13343404337304794372'),
    ('ut', '1019'),
    ('appid', '0'),
    ('refer', 'https://ssl.captcha.qq.com/cap_union_new_show'),
    ('domain', 'ssl.captcha.qq.com'),
    ('fph', ''),
    ('fpv', '0.0.15'),
    ('ptcz', ptcz),
    ('callback', '_fp_041413'),
)

response = sess.get('https://ssl.captcha.qq.com/dfpReg', headers=headers, params=params, cookies=cookies)


respdata = json.loads(response.content.decode("utf-8").replace("_fp_041413(","")[:-1])

fpsig = respdata['fpsig']









params = (
    ('aid', '2100049390'),
    ('protocol', 'https'),
    ('accver', '1'),
    ('showtype', 'popup'),
    ('ua', 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NzUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83NS4w'),
    ('noheader', '1'),
    ('fb', '1'),
    ('enableDarkMode', '0'),
    ('fpinfo', 'fpsig='+fpsig),
    ('grayscale', '1'),
    ('clientype', '2'),
    ('subsid', '2'),
    ('sess', sess_),
    ('fwidth', '0'),
    ('sid', sid),
    ('forcestyle', 'undefined'),
    ('wxLang', ''),
    ('tcScale', '1'),
    ('uid', '2819700269'),
    ('cap_cd', ''),
    ('rnd', '499769'),
    ('TCapIframeLoadTime', 'undefined'),
    ('prehandleLoadTime', '30'),
    ('createIframeStart', createIframeStart),
    ('ptcz',ptcz)
)

capHtml = sess.get('https://ssl.captcha.qq.com/cap_union_new_show', headers=headers, params=params)
capHtml = capHtml.content.decode("utf-8")

txt = re.findall('dt="(.*?)"',capHtml,re.S)
print("规则",txt)

is_coding = False
for r in ["请点击正对着你的","请点击侧对着你的"]:
  if r in txt[0]:
    is_coding= True

if not is_coding:
  print("未编写改代码")
  exit()


jspath = re.findall("tdc.js(.*?)>",capHtml,re.S)

websig = re.findall("websig:\"(.*?)\"",capHtml,re.S)[0]

vsig = re.findall('H="(.*?)"',capHtml,re.S)[0]

print(jspath)















jspath = "https://ssl.captcha.qq.com/tdc.js"+jspath[0]

with open("html.html","w") as f:
  f.write(response.content.decode("utf-8").replace(jspath,"tdc.js"))





stage_str = """
window = {}
var window = {}

window['Array'] = Array

window.navigator = {}
window.navigator.cookieEnabled = true
window.location = {}
window.location.href = ""
window.getComputedStyle = function(){return {}}
window.matchMedia = function(x){
    return {media: x,matches:true}
}
var document = {}
document.documentElement = {}
document.charset = "UTF-8"
window.innerWidth = 1920
window.innerHeight = 937
document.documentElement.clientWidth = 1903
document.documentElement.clientHeight = 937
document.body = {}
document.body.clientWidth = 1903
document.body.clientHeight = 1889
document.body = {}
document.body.clientWidth = 476
document.body.clientHeight = 137
document.createElement = function(){return []}
navigator = {}
navigator.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
screen = {
    availHeight: 1040,
    availLeft: 0,
    availTop: 0,
    availWidth: 1920,
    colorDepth: 24,
    height: 1080,
    left: 0,
    mozOrientation: "landscape-primary",
    onmozorientationchange: null,
    pixelDepth: 24,
    top: 0,
    width: 1920,
    orientation: {angle: 0,type: "landscape-primary"}
}
window.screen = screen
document.createElement = function (x) { return [] }
"""

stage_str += 'document.cookie = "{}"\n\n\n'.format(cookie_str)

end_str = """

Z = 1    
TDC = window['TDC']

TDC.setData("ft","6f_7P_n_H")
TDC.setData({coordinate:[10, 64, "0.5000"]})
K = 0
function add_x(){

TDC.setData({
                trycnt: ++Z,
                refreshcnt: K
            })
gdata = TDC.getData()
return [TDC.getInfo()['info'],gdata];


}

x = add_x()
console.log(x)

"""

jsresp = sess.get(jspath)
print(sess.cookies)


with open("tdc.js","w") as f:
  f.write(stage_str + jsresp.content.decode("utf-8") + end_str)


import execjs
ctx = execjs.compile(open("tdc.js","r").read())



params = (
    ('aid', '2100049390'),
    ('protocol', 'https'),
    ('accver', '1'),
    ('showtype', 'popup'),
    ('ua', 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NzUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83NS4w'),
    ('noheader', '1'),
    ('fb', '1'),
    ('enableDarkMode', '0'),
    ('fpinfo', 'fpsig=undefined'),
    ('grayscale', '1'),
    ('clientype', '2'),
    ('subsid', '3'),
    ('sess', sess_),
    ('fwidth', '0'),
    ('sid', sid),
    ('forcestyle', 'undefined'),
    ('wxLang', ''),
    ('tcScale', '1'),
    ('uid', '2819700269'),
    ('cap_cd', ''),
    ('rnd', '499769'),
    ('TCapIframeLoadTime', 'undefined'),
    ('prehandleLoadTime', '30'),
    ('createIframeStart', '1587446299561'),
    ('rand', '0.726533437089379'),
    ('vsig', vsig),
)



response = sess.get('https://ssl.captcha.qq.com/cap_union_new_getcapbysig', headers=headers, params=params, cookies=cookies)


with open("t.jpg","wb") as f:
  f.write(response.content)







objects = p("t.jpg")

'''
[{'name': 'zhengdui', 'x1': 141.91305541992188, 'x2': 207.52615356445312, 'y1': 182.9700469970703, 'y2': 289.5917663574219}, {'name': 'yuanzhui', 'x1': 539.66796875, 'x2': 644.810546875, 'y1': 222.9202880859375, 'y2': 328.2587890625}, {'name': 'zhengdui', 'x1': 488.8005065917969, 'x2': 554.8145751953125, 'y1': 80.8041763305664, 'y2': 190.52880859375}, {'name': 'cedui', 'x1': 129.19741821289062, 'x2': 177.7596435546875, 'y1': 83.20233917236328, 'y2': 201.85980224609375}, {'name': 'zhengdui', 'x1': 545.4267578125, 'x2': 640.708984375, 'y1': 218.67037963867188, 'y2': 329.60302734375}, {'name': 'yuanti', 'x1': 384.8795166015625, 'x2': 481.59320068359375, 'y1': 215.79359436035156, 'y2': 311.32647705078125}, {'name': 'zhengfangti', 'x1': 385.5037536621094, 'x2': 474.96282958984375, 'y1': 212.2169647216797, 'y2': 308.42047119140625}, {'name': 'zhengdui', 'x1': 330.2404479980469, 'x2': 387.6609191894531, 'y1': 130.0834503173828, 'y2': 261.6133728027344}, {'name': 'zhengdui', 'x1': 229.5642852783203, 'x2': 286.5433044433594, 'y1': 146.38681030273438, 'y2': 273.88916015625}]
'''

all_ans = []
if "正" in txt[0]:
  for o in objects:
    if o['name'] == 'zhengdui':
      ans = "{},{};".format(int((o['x1']+o['x2'])/2),int((o['y1']+o['y2'])/2))
      all_ans.append(ans)
      print("ans:",ans)



if "请点击侧" in txt[0]:
  for o in objects:
    if o['name'] == 'cedui':
      ans = "{},{};".format(int((o['x1']+o['x2'])/2),int((o['y1']+o['y2'])/2))
      print("ans:",ans)
      all_ans.append(ans)




def verif(gdata,ans,eks):
  params = (
      ('random', '1587460707166'),
  )

  data = {
    'aid': '2100049390',
    'protocol': 'https',
    'accver': '1',
    'showtype': 'popup',
    'ua': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NzUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC83NS4w',
    'noheader': '1',
    'fb': '1',
    'enableDarkMode': '0',
    'fpinfo': 'fpsig='+fpsig,
    'grayscale': '1',
    'clientype': '2',
    'subsid': '5',
    'sess': sess_,
    'fwidth': '0',
    'sid': sid,
    'forcestyle': 'undefined',
    'wxLang': '',
    'tcScale': '1',
    'uid': '2819700269',
    'cap_cd': '',
    'rnd': '499769',
    'TCapIframeLoadTime': 'undefined',
    'prehandleLoadTime': '30',
    'createIframeStart': createIframeStart,
    'subcapclass': '11',
    'vsig': vsig,
    'ans': ans,
    'cdata': '12',
    'accbcb': gdata,
    'websig': websig,
    'eks':eks,
    'tlg': '1',
    'vlg': '0_1_0',
    'vmtime': '_',
    'vmData': ''
  }

  response = sess.post('https://ssl.captcha.qq.com/cap_union_new_verify', headers=headers, params=params, cookies=cookies, data=data)



  jsondata = json.loads(response.content.decode('utf-8'))
  print(jsondata)
  if jsondata['errorCode'] == '0':
    print("验证通过")
    exit()





eks,gdata = ctx.call("add_x")
# print(eks)
# print(gdata)

for r in all_ans:
  verif(gdata,r,eks)
  eks,gdata = ctx.call("add_x")
  # print(eks)
  # print(gdata)


