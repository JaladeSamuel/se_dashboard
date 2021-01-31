/*
   SVG to Canvas 
   through JavaScript objets
   
   This lib convert SVG tags to Canvas commands
   once the SVG file est stored in a JS object
   by the Scriptol compiler.
*/

function canvasInit(id) {
    return document.getElementById(id).getContext("2d")
}

// Get values from a simple path - Thanks Cletus at S.O.
function parsePath(d) {
    var a = []
    var r = /\d+/g;
    var m;
    while ((m = r.exec(d)) != null) {
        a.push(m[0]);
    }   
    return a 
}

function SVGtoCanvas(el, ctx, xo, yo) {
    var tag 
    var x, x2, y, y2, cx, cy, rx, ry, w, h
    var data, font, arr, path
    var fillFlag=false
    ctx.save()  
    ctx.beginPath()  
    for(var att in el) {
       var val = el[att]
       switch(att) {
       case 'tag':
            tag = val
            break
       case 'data':
            data = val            
       case 'stroke':
            ctx.strokeStyle=val
            break
       case 'stroke-width':
            ctx.lineWidth=val
            break
       case 'fillStyle':
       case 'fill':
            if(val=="none") val="transparent"
            ctx.fillStyle=val
            fillFlag=true
            break                
       case 'x':
       case 'x1':
            x = Number(val) + xo
            break
       case 'y':     
       case 'y1':
            y = Number(val) + yo
            break
       case 'x2':
            x2 =Number(val) + xo
            break
       case 'y2':
            y2 = Number(val) + yo
            break
       case 'cx':
            cx = Number(val) + xo
            break
       case 'cy':
            cy = Number(val) + yo
            break                
       case 'rx':
            rx = val
            break
       case 'ry':
            ry = val
            break                  
       case 'width':
            w = val
            break
       case 'height':
            h = val
            break
       case 'style':
            break
       case 'd':
             path = val
             break
       case 'font-size':
            font = val + "px Calibri Arial"  
            break;   
       default:
            if(val instanceof Object || typeof val == "object")  {
                 SVGtoCanvas(val, ctx, xo, yo)    
            }            
            continue;     
       } 
    }
    switch(tag) {
        case 'line':
            ctx.moveTo(x,y)
            ctx.lineTo(x2,y2)
            ctx.stroke()
            break;
        case 'circle':
            ctx.arc(cx, cy, rx, 0, 2 * Math.PI);
            ctx.stroke();                
            break;
        case 'ellipse':  
            ctx.scale(1, ry / rx)
            ctx.arc(cx, cy, rx, 0, 2 * Math.PI);
            ctx.stroke();
            break;
        case 'rect':
            ctx.rect(x, y, w, h);
            ctx.stroke();                 
            break;
        case 'path':
            arr = parsePath(path);
            ctx.moveTo(Number(arr[0]) + xo, Number(arr[1])+ yo)
            ctx.bezierCurveTo(Number(arr[2])+xo, Number(arr[3])+yo, 
            Number(arr[4])+xo, Number(arr[5])+yo, Number(arr[6])+xo, Number(arr[7])+yo)
            ctx.stroke()
            break       
        case 'text':
            ctx.font = font
            ctx.strokeText(data, x, y);
            break;    
        case 'g':
            break;
        default:
            break;    
   }
   if(fillFlag) ctx.fill()
   ctx.restore()        
}