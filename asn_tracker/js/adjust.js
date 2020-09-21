function master_onload(obj)
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

function slave_onload(obj)
{
    console.log("slave_onload");
    obj.contentWindow.onhashchange = function(){
        window.scrollTo(0, 0); 
    }
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

    document.querySelector("#slave").contentWindow.onhashchange = function(){
        window.scrollTo(0, 0); 
    }

};
