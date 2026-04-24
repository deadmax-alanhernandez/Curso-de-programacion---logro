console.log ("Reto FizzBuzz")


for (let it = 1; it < 50; it++) {
    

  if (it % 3 === 0 && it % 5 === 0) {
    console.log("FizzBuzz");
  } 
 
  else if (it % 3 === 0) {
    console.log("Fizz");
  } 
  
  else if (it % 5 === 0) {
    console.log("Buzz");
  } 
 
  else {
    console.log(it);
  }
}