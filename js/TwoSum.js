/**

 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (complement in map) {
      console.log([map[complement], i]);
      return [map[complement], i];
    }
    map[nums[i]] = i;
  }
};
