/**
 * Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100s]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {

    let unsrtdArr=[]
    nums.map(function(num){
        unsrtdArr.push(num*num)
    })
    
    unsrtdArr.sort(function(a, b) {
        return a - b;
      });

    return unsrtdArr
};

sortedSquares([-4,-1,0,3,10])