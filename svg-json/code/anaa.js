
/**
	AnAA - Ajax Framework
	Version 1.7
	www.anaa.eu
	(c) 2007-2008 Sandrine Takis and Denis Sureau.
	Free under the GNU GPL 2.0 Licence.
*/	

var AACaching = false;


function AACreate() 
{
    var request = false;
        try {
            request = new ActiveXObject('Msxml2.XMLHTTP');
        }
        catch (err2) {
            try {
                request = new ActiveXObject('Microsoft.XMLHTTP');
            }
            catch (err3) {
		try {
			request = new XMLHttpRequest();
		}
		catch (err1) 
		{
			request = false;
		}
		}
	}
    return request;
}


/**
	AA Read
	Load a file, text or XML
*/	

function AARead(url, fun, element)
{ 
	var xhr = AACreate();
	var ext = url.substr(url.length - 3);
	var isXML =  (ext == "xml");	

	xhr.onreadystatechange=function()
	{ 
		if(xhr.readyState == 4)
		{
			if(xhr.status == 200)
			{
				var content;
				if(isXML) 
					content = xhr.responseXML;
				else
					content = xhr.responseText;
				fun(content, element);
			}
		} 
	}; 

	if(AACaching == false)
		url = url + "?nocache=" + Math.random();
	xhr.open("GET", url , true);
	xhr.send(null); 
} 

/**
	Read an XML file with any extension
*/

function AALoadXML(url, fun, element)
{ 
	var xhr = AACreate();
	xhr.onreadystatechange=function()
	{ 
		if(xhr.readyState == 4)
		{
			fun(xhr.responseXML, element);
		} 
	}; 
	xhr.open("GET", url , true);
	xhr.send(null); 
} 

/**
	AAWrite
	url:	the script
	data:	the string to pass to the script
		it is a list of pairs x=y separated by &
*/	

function AAWrite(url, data, fun)
{ 
	var xhr = AACreate();

	xhr.onreadystatechange=function()
	{ 
		if(xhr.readyState == 4)
		{
			if(fun != null) fun();
		}
	}; 
	xhr.open("POST", url, true);		
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	xhr.send(data); 
} 
	

function AAGetBody(content)
{
	var x = content.indexOf("<body");
	if(x == -1) return "";
		
	x = content.indexOf(">", x);
	if(x == -1) return "";

	var y = content.lastIndexOf("</body>");
	if(y == -1) return "";
	
	return content.slice(x + 1, y);
}

function AAPutHTML(content, target)
{
	target.innerHTML = AAGetBody(content);
}

/**
	Loads a HTML page
	Put the content of the body tag into the current page.
	Arguments:
		url of the other HTML page to load
		id of the tag that has to hold the content
*/		

function AALoadHTML(url, fun, storage, param)
{
	var xhr = AACreate();
	xhr.onreadystatechange=function()
	{ 
		if(xhr.readyState == 4)
		{
			if(xhr.status == 200)
			{
				storage = document.getElementById(storage);
				storage.innerHTML = AAGetBody(xhr.responseText);
				fun(storage, param);
			}
		} 
	}; 

	if(AACaching == false)
		url = url + "?nocache=" + Math.random();
	xhr.open("GET", url , true);
	xhr.send(null); 

} 


/**
	Send a HEAD request,
	call a function with the value 
*/

function AAHead(url, key, fun, element)
{ 
	var xhr = AACreate();

	xhr.onreadystatechange = function() 
	{
		if(xhr.readyState == 4) 
		{
			var value;
			if (xhr.status == 200)
			{ 
				 value = xhr.getResponseHeader(key);
			}
			else 
			{
				if(xhr.status==404) 
					value = url + " doesn't exist!";
				else 
					value = "Error, status is " + xhr.status;
			}
			fun(value, element);		
		}
	}
	xhr.open("HEAD", url, true);
	xhr.send(null); 
} 

