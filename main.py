function findMaxNumber(numbers) {
  if (numbers.length === 0) {
    return null; // Return null if the array is empty
  }

  let max = numbers[0]; // Assume the first element is the maximum

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i]; // Update the maximum if a larger number is found
    }
  }

  return max; // Return the maximum number
}

// Example usage:
const numbersArray = [3, 9, 12, 5, 1, 7];
const maxNumber = findMaxNumber(numbersArray);
console.log("The maximum number is:", maxNumber);
