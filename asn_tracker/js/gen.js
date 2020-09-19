
function fill_asn_items(obj)
{
    var child;
    var text;

    child = document.createElement('a');
    child.className = "w3-bar-item w3-button";
    child.onclick = change_asn;
child.text = "EUTRA-InterNodeDefinitions";child.href= "#";obj.appendChild(child);
    child = document.createElement('a');
    child.className = "w3-bar-item w3-button";
    child.onclick = change_asn;
child.text = "NR-InterNodeDefinitions";child.href= "#";obj.appendChild(child);
    child = document.createElement('a');
    child.className = "w3-bar-item w3-button";
    child.onclick = change_asn;
child.text = "NR-RRC-Definitions";child.href= "#";obj.appendChild(child);
    child = document.createElement('a');
    child.className = "w3-bar-item w3-button";
    child.onclick = change_asn;
child.text = "EUTRA-RRC-Definitions";child.href= "#";obj.appendChild(child);
}