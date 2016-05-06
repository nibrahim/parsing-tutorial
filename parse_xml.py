from xml.etree import ElementTree

tree = ElementTree.parse('sample.xml')

root = tree.getroot()

# Iterating
for country in root:
    print "Country : {}".format(country.attrib['name'])
    for data in country:
        print "  {:8} : {}".format(data.tag, data.text)

# Searching
# Find tags from a root that match a name.
for i in root.iter('rank'):
    print i.text

# Find first child
x = root.find("country")
print x
print x.get('name')

# Find all children
print root.findall("country")

# Modifying
for i in root.findall("country"):
    i.set("active", "true")

tree.write("sample2.xml")





