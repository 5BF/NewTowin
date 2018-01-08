import xml.dom.minidom

dom=xml.dom.minidom.parse('web.xml')

root=dom.documentElement

tagname=root.getElementsByTagName('maxid')

print(tagname[0].tagName)

tagname=root.getElementsByTagName('caption')
tagname2=dom.getElementsByTagName('caption')
print(tagname[1].tagName)
print(tagname[2].tagName)
print(tagname2[2].firstChild.data)

logins=root.getElementsByTagName('login')
username=logins[0].getAttribute("username")
print(username)