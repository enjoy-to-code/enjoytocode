let intArray =[ 1, 4, 6, 7, 12, 15, 23, 25, 28, 29, 30 ];
let searchNumber = 28;

let binarySearch = function (intArray, start, end, searchNumber) {
    // check if array has more than one element
    if (start > end) return false;
   
    // calculate middle of array
    let mid=Math.floor((start + end)/2);
   
    // Compare mid with given searchNumber
    if (intArray[mid]===searchNumber) return true;
          
    // If mid > searchNumber, select left half of intArray
    if(intArray[mid] > searchNumber) 
        return binarySearch(intArray, start, mid-1, searchNumber);
    else
        // else select right half intArray
        return binarySearch(intArray, mid+1, end, searchNumber);
}
   
if (binarySearch(intArray, 0, intArray.length-1, searchNumber))
    console.log("Element found!");
else console.log("Element not found!");
   