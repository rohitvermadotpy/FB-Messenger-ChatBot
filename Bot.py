from Component import com


FB_Token = "your_page_access_token"


COM = com(FB_Token)


def echo(data):
    fdata = COM.parse(data)
    uid = fdata["uid"]
    text = fdata["text"]

    COM.markMessageRead(uid)
    COM.sendmsg(uid, text)
