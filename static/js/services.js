'uses strict';


      function expand(){
        var j=0;
        var i = document.getElementById("menu").childNodes;
      if(j==0){
        document.getElementById("add").style.transform = 'rotate(45deg)';
        j=1;
        i[1].style.transform = 'translateY(-160px)';
      }
      else{
        document.getElementById("add").style.transform = 'rotate(0deg)';
        j=0;
      }
      console.log("acho")
     }

  