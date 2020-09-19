function link_slave(obj)
{
    let doc = obj.contentDocument;
    console.log(doc);
    let items = doc.querySelectorAll("a");
    
    for (let item of items)
    {
    //    console.log(item);
        item.target = "slave";
    }

    //console.log(obj);
}

function change_asn()
{
    var master = document.getElementById("master");
    var slave = document.getElementById("slave");
    master.src = "html/"+this.text+".html";
    slave.src = "html/"+this.text+".html";
}

window.onload = function() {

    var seleciton = document.getElementById("id_selection");
    console.log(seleciton);
    fill_asn_items(seleciton);

};
