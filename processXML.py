import xml.etree.ElementTree as ElementTree
def read_xml(path):
    tree = ElementTree.parse(path)
    root = tree.getroot()
    student  = root.findall('student')
    for item in student:
        print("id = {}, name = {}".format(item.find('id').text,item.find('name').text))
def write_xml(path,data):
    parent = ElementTree.Element('students')
    children = ElementTree.SubElement(parent, 'student')
    comment = ElementTree.Comment('user comment')
    parent.append(comment) #this comment will be appended to parent element
    # insert key
    id_node = ElementTree.Element('id')
    name_node = ElementTree.Element('name')
    children.append(id_node)
    children.append(name_node)
    #insert data
    children.find('id').text = data['id']
    children.find('name').text = data['name']
    # dump tree
    ElementTree.dump(children)
    tree = ElementTree.ElementTree(parent)
    tree.write(path)
if __name__ == '__main__':
    path = 'xml\\myXMLFile.xml'
    read_xml(path)
    #insert data
    data1 = {'id':'002','name':'Anh'}
    data2 = {'id':'004','name':'Anh'}
    write_xml("xml\\outputXML.xml",data1)
    write_xml("xml\\outputXML.xml",data2)

    