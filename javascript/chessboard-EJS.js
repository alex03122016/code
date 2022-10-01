size = 12
for (let y = 0; y < size; y = y+1){
  if (y%2==0){
     outputEven =""
    for (let x = 0; x < (size/2); x= x + 1){
      outputEven = outputEven + "# "
    }
    console.log(outputEven)
  }
  else{
    outputOdd=""
    for(let x = 0; x < (size/2); x = x+1){
      outputOdd = outputOdd + " #"
    }
    console.log(outputOdd)
  }
    }
