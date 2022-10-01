function isEven(n){
  if (n == 0){
    return console.log("is Even");
  }
  if (n == 1){
    return console.log("is Odd");
  }
  else{
    //console.log(n)
    return isEven(n - 2)
  }

}

isEven(41199)
