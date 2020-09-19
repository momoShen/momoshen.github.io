import os, re
import fnmatch

in_folder = "./asn"
out_folder = "./html"
js_folder = "./js"

def get_items(data) :
    it = re.finditer("^(\S+).*::=", data, re.MULTILINE) # BCCH-BCH-MessageType ::=  
    items = []
    for match in it :
        if not re.match('^--', match.group()) :
            item = match.group(1)
            items.append(item)
            #print(item)
    
    print("[STEP] get_items done: num="+str(len(items)))

    return items

def modify_content(data, items) :

    content = ""
    for line in data.splitlines() :
        line = re.sub(r'(--(.*))', r'<span class="nocode">\1</span>', line); # comment
        content += re.sub(r'(\S+)(\s+)(.*)::=', r'<span id="id_\1">\1</span>\2\3::=', line) + "\n"; # item   

    data = content

    for item in items:
        data = re.sub(r'([\s]+)'+item+r'([\s|,]+)', r'\1<a href="#id_'+item+r'">'+item+r'</a>\2', data) # link

    print("[STEP] modify_content done")

    return data

def gen_script(items) :
    out_file = os.path.join(js_folder, "gen.js")
    with open(out_file, "w") as out_fn :    
        content = '''
function fill_asn_items(obj)
{
    var child;
    var text;
'''    
        for item in items :
            content += '''
    child = document.createElement('a');
    child.className = "w3-bar-item w3-button";
    child.onclick = change_asn;
'''
            content += r'child.text = "'+item+r'";'
            content += r'child.href= "#";'

            #content += r'''child = document.createTextNode('<a href="#" class="w3-bar-item w3-button">'''+item+r'''</a>');'''
            content += r'obj.appendChild(child);'
        content += '''
}'''
        out_fn.write(content)

def eth_main() :

    items = gen_file()
    gen_script(items)

def gen_file() :

    results = []

    for root, dirs, files in os.walk(in_folder) :

        for asn in files :
            if fnmatch.fnmatch(asn, "*.asn") :

              #  if not re.search(r'InterNode', asn) :
              #      continue

                match = re.match(r'(.*)\.asn', asn)
                name = match.group(1)
                print(name)
                in_file = os.path.join(in_folder, name+".asn")
                out_file = os.path.join(out_folder, name+".html")
                with open(in_file, 'r') as in_fn, open(out_file, 'w') as out_fn:
                    data = in_fn.read()

                    for encoding in ('utf-8', 'windows-1252'):
                        try:
                            data = data.decode(encoding)
                            break
                        except:
                            warnings.warn_explicit("Decoding %s as %s failed, trying next." % (fn, encoding), UserWarning, '', 0)

                    if not isinstance(data, str):
                        data = data.encode('utf-8')

                    items = []

                    items = get_items(data)
                    
                    data = modify_content(data, items)
                    html = r'<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>'
                    #html = ""
                    html += "<pre class='prettyprint'>"+data+"</pre>" 
                    out_fn.write(html)
                    
                    results.append(name)
    return results

#--- BODY ---------------------------------------------------------------------

if __name__ == '__main__':
    eth_main()


