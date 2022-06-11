//write your JS code here:






function Activity (dict){
    
    dict.forEach(element => {
        switch (element.operation){
        case "+":
            console.log(element.data.reduce((partialSum, a) => partialSum + a, 0))
            break
        case "*":
            console.log(element.data.reduce((a, b)=> a*b, 1))
            break
        case "push":
            console.log(`[${[...element.data[0],...element.data.slice(1)]}]`)
            break
        case "filter":
            console.log(`[${element.data[0].filter((value) => !element.data.slice(1).includes(value))}]`)
            break
        case "merge":
            console.log(`[${[].concat(...element.data)}]`)
            break
        }
    });
}


const OPERATIONS = [
    {operation: "push", data: [[1, 2, 3], 4]},
    {operation: "+", data: [1, 2, 3]},
    {operation: "+", data: [3]},
    {operation: "*", data: [2, 3]},
    {operation: "filter", data: [[1, 2, 3], 3]},
    {operation: "merge", data: [[1, 2, 3], [4, 5], [6], [7]]},
];
Activity(OPERATIONS)