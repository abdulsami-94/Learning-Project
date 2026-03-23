// Plain JS
/*
let score = 0 ;
function greet(name) {
    return "Hello" + name;
}
*/



let score: number = 0;
function greet(name: string): string{
    return "hello " + name;
}



// Comman Types
let age: number = 25;
let username: string = "Alice";
let isLoggedIn: boolean = true;
let scores: number[] = [10, 20, 30]; //Array of Numbers
let pair: [string, number] = ["hp", 100];   //Tuple



// Interfaces - shape of an object
interface User {
    id: number;
    name: string;
    email?: string //? means Optional
}

const user: User = {id: 1, name: "Alice"};



// Union Types
let input: string | number;
input = "hello";    // Fine
input = 42;     // also fine
input = true;    // Error



//Type Inference
let count = 0;
count = "opps"; //Error -- even without me writting : number



