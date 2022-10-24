/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function (arr) {
  var indexes = [];
  var lengthArr = arr.length;
  console.log(lengthArr);

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == 0) {
      indexes.push(i);
    }
  }

  for (let index = 0; index < indexes.length; index++) {
    arr.splice(indexes[index] + index, 0, 0);
  }

  arr.length = lengthArr;

  return arr;
};

duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]);
