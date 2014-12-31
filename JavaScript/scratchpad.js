console.log('Scratchpad Script is now running!');

var code = prompt("Continue with the code stuff?") 

    if(code === "yes" || code === "Yes")
        {  
             console.log('Yey Script time!');

             var yey = prompt("Yey?")
                if(yey === "yey" || yey === "Yey")
                    {
                         alert("This makes me happy!");
                    }
                else
                    {
                        alert("You make me sad now....");
                    }
         }


    else if(code === "no" || code === "No")   
        {
            console.log('Really I cant show you my coding things?');

            alert("aaw...no code stuff");
        }
    else if(code === null)
        {
            console.log("User cancled the diolog Box");
        }
    else
        {
            console.log('Error no recgonized input!');
            
            alert("Error, Invalid input");
        }
