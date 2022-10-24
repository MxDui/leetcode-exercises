var findNumbers = function (nums) {

    var evenDigits = []; 
    var evenNumbers;
    
    for (let i = 0; i < nums.length; i++) {
        let currDigitNumber = nums[i].toString().length
        console.log(currDigitNumber)
     
        if (currDigitNumber % 2 === 0) {
             evenDigits.push(currDigitNumber % 2 === 0)
        } else {
            evenNumbers = 0
        }

    }
    return evenDigits.length
};

findNumbers([12, 345, 2, 6, 7896]);