from urllib import request
import json
resp = request.urlopen("http://127.0.0.1:4040/api/tunnels")
data = json.load(resp)
tunnels = data["tunnels"]
url = tunnels[0]['public_url']
server = url[6:]
# print(server)


m = "screen mode id: i: 2\nuse multimon: i: 0\ndesktopwidth: i: 1280\ndesktopheight: i: 720\nsession bpp: i: 32\nwinposstr: s: 0, 1, 310, 56, 1110, 656\ncompression: i: 1\nkeyboardhook: i: 2\naudiocapturemode: i: 0\nvideoplaybackmode: i: 1\nconnection type: i: 7\nnetworkautodetect: i: 1\nbandwidthautodetect: i: 1\ndisplayconnectionbar: i: 1\nenableworkspacereconnect: i: 0\ndisable wallpaper: i: 0\nallow font smoothing: i: 0\nallow desktop composition: i: 0\ndisable full window drag: i: 1\ndisable menu anims: i: 1\ndisable themes: i: 0\ndisable cursor setting: i: 0\nbitmapcachepersistenable: i: 1\naudiomode: i: 0\nredirectprinters: i: 1\nredirectcomports: i: 0\nredirectsmartcards: i: 1\nredirectclipboard: i: 1\nredirectposdevices: i: 0\nautoreconnection enabled: i: 1\nauthentication level: i: 2\nprompt for credentials: i: 0\nnegotiate security layer: i: 1\nremoteapplicationmode: i: 0\nalternate shell: s:\nshell working directory: s:\ngatewayhostname: s:\ngatewayusagemethod: i: 4\ngatewaycredentialssource: i: 4\ngatewayprofileusagemethod: i: 0\npromptcredentialonce: i: 0\ngatewaybrokeringtype: i: 0\nuse redirection server name: i: 0\nrdgiskdcproxy: i: 0\nkdcproxyname: s:\ndrivestoredirect: s:\nusername:s:ayush\n"

text_file = open("sample.rdp", "w")
n = text_file.write(m+"full address:s:"+server)
text_file.close()


plaintext = text.decode('utf8')
links = re.findall("href=[\"](.*?)[\"]", plaintext)
print(links[:5])
