


/*
A function that accepts a number of U.S. cents and returns an 
    array containing, respectively, the smallest number of U.S. 
    quarters, dimes, nickels, and pennies that equal the given amount. 

Input: # of US cents 
Return [quarters, dimes, nickels, pennies]
*/
function change(centsTot){
    //since this is for a given set of denominations, 
    //  I will use simple solution not a general knapscak soln

    denomVal = [25, 10, 5, 1]   //stores the values of the denominations in decreasing order
    denomUsed = [0,0,0,0]       //stores how many of each respective denomination was used

    //were I /really/ getting into this program:
    //console.assert(denomVal.length == denomName.length)
    //console.assert(denomName.length == denomUsed.length)

    //i guess I should check denomVal is ordered here but.. 
    //  waste for such a simple exercise


    counter = centsTot
    for(i = 0 ; i < denomVal.length ; i++)
    {
        temp = floor(counter/denomVal[i])
        counter -= temp*denomVal[i]
        denomUsed[i] = temp
    }

    return denomUsed
}