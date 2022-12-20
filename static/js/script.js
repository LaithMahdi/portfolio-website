// get value of range of Compétences  
function rangefn(){
    document.getElementById("label").innerHTML=document.getElementById("rang_val").value;
}

// disabled and enable option of list in Compétences 
function selectType(){
    liste=document.getElementById("D").value;
    if (liste=='2')
    {
        document.getElementById("rang_val").disabled=true;
        document.getElementById("label").innerHTML=document.getElementById("rang_val").value="None";
    }
    else 
    {
        document.getElementById("rang_val").disabled=false;
        document.getElementById("label").innerHTML=document.getElementById("rang_val").value;
    }
}


// Show add description button 
function CountRows() {
    var totalRowCount = 0;
    var rowCount = 0;
    var table = document.getElementById("table");
    var rows = table.getElementsByTagName("tr")
    for (var i = 0; i < rows.length; i++) {
        totalRowCount++;
        if (rows[i].getElementsByTagName("td").length > 0) {
            rowCount++;
        }
    }
    var message = "Total Row Count: " + totalRowCount;
    message += "\nRow Count: " + rowCount;
    console.log(message);

    if (rowCount>0)
        document.getElementById("ajouterBtn").style.display="none";
    else
        document.getElementById("ajouterBtn").style.display="";
}

